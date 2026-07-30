#!/usr/bin/env python3
"""
resume_analyzer.py
==================

Detailed resume analysis tool for PDF and DOCX files.

Extracts (regardless of the specific template/style used):
    - Name
    - Contact info (email, phone, LinkedIn, GitHub, portfolio, location)
    - Professional summary / objective
    - Skills (normalized, deduplicated)
    - Work experience (title, company, start/end dates, duration, description)
    - Education (degree, field, institution, year)
    - Certifications
    - Projects
    - Languages
    - Total years of professional experience

All extracted values are normalized:
    - Dates      -> "YYYY-MM" (or "Present")
    - Phone      -> "+<countrycode> <national number>" best-effort E.164-like form
    - Degrees    -> full canonical names (e.g. "B.Tech" -> "Bachelor of Technology")
    - Skills     -> lowercase, de-duplicated, common aliases merged (e.g. "js" -> "javascript")
    - Emails/URLs-> lowercased, trimmed

Dependencies (install once):
    pip install pdfplumber python-docx phonenumbers --break-system-packages
    (phonenumbers is optional but strongly recommended for correct phone
    number normalization; a regex-based fallback is used if it's missing)

Usage:
    python resume_analyzer.py path/to/resume.pdf
    python resume_analyzer.py path/to/resume.docx --out result.json

Note on accuracy:
    Resume layouts vary enormously (columns, tables, icons instead of labels,
    creative graphic templates, etc.). This tool uses a layered strategy —
    explicit section headers first, then regex/keyword heuristics, then
    positional fallbacks — to cover the large majority of common formats.
    No rule-based (non-ML) parser can be 100% accurate on every template;
    review the output, especially for highly graphical/creative resumes.
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict, Any


# --------------------------------------------------------------------------
# 1. TEXT EXTRACTION (PDF / DOCX -> plain text, line-preserving)
# --------------------------------------------------------------------------

def extract_text_from_pdf(path: str) -> str:
    """Extract text from a PDF, preserving line/layout structure as best as possible."""
    try:
        import pdfplumber
    except ImportError:
        sys.exit("Missing dependency: pip install pdfplumber --break-system-packages")

    lines = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            # x_tolerance/y_tolerance defaults work well for most resumes;
            # layout=True-like behavior approximated via extract_text()
            text = page.extract_text(x_tolerance=1, y_tolerance=3) or ""
            lines.append(text)
    return "\n".join(lines)


def extract_text_from_docx(path: str) -> str:
    """Extract text from a DOCX, including text inside tables (common in resumes)."""
    try:
        import docx
    except ImportError:
        sys.exit("Missing dependency: pip install python-docx --break-system-packages")

    document = docx.Document(path)
    lines = []

    def iter_block_items(doc):
        # Walk the document body in order, handling both paragraphs and tables.
        from docx.oxml.ns import qn
        from docx.table import Table
        from docx.text.paragraph import Paragraph
        parent_elm = doc.element.body
        for child in parent_elm.iterchildren():
            if child.tag == qn('w:p'):
                yield Paragraph(child, doc)
            elif child.tag == qn('w:tbl'):
                yield Table(child, doc)

    for block in iter_block_items(document):
        if hasattr(block, "text"):  # Paragraph
            if block.text.strip():
                lines.append(block.text.strip())
        else:  # Table
            for row in block.rows:
                cells = [c.text.strip() for c in row.cells if c.text.strip()]
                if cells:
                    lines.append(" | ".join(cells))

    return "\n".join(lines)


def extract_text(path: str) -> str:
    ext = Path(path).suffix.lower()
    if ext == ".pdf":
        return extract_text_from_pdf(path)
    elif ext in (".docx", ".doc"):
        if ext == ".doc":
            sys.exit("Legacy .doc is not supported — please convert to .docx or .pdf.")
        return extract_text_from_docx(path)
    else:
        sys.exit(f"Unsupported file type: {ext}. Use .pdf or .docx")


# --------------------------------------------------------------------------
# 2. NORMALIZATION HELPERS
# --------------------------------------------------------------------------

MONTHS = {
    "jan": "01", "january": "01", "feb": "02", "february": "02",
    "mar": "03", "march": "03", "apr": "04", "april": "04",
    "may": "05", "jun": "06", "june": "06", "jul": "07", "july": "07",
    "aug": "08", "august": "08", "sep": "09", "sept": "09", "september": "09",
    "oct": "10", "october": "10", "nov": "11", "november": "11",
    "dec": "12", "december": "12",
}

DEGREE_MAP = {
    "b.tech": "Bachelor of Technology", "btech": "Bachelor of Technology",
    "b.e": "Bachelor of Engineering", "be": "Bachelor of Engineering",
    "m.tech": "Master of Technology", "mtech": "Master of Technology",
    "m.e": "Master of Engineering", "me": "Master of Engineering",
    "b.sc": "Bachelor of Science", "bsc": "Bachelor of Science",
    "m.sc": "Master of Science", "msc": "Master of Science",
    "b.a": "Bachelor of Arts", "ba": "Bachelor of Arts",
    "m.a": "Master of Arts", "ma": "Master of Arts",
    "b.com": "Bachelor of Commerce", "bcom": "Bachelor of Commerce",
    "m.com": "Master of Commerce", "mcom": "Master of Commerce",
    "mba": "Master of Business Administration",
    "bba": "Bachelor of Business Administration",
    "phd": "Doctor of Philosophy", "ph.d": "Doctor of Philosophy",
    "bca": "Bachelor of Computer Applications",
    "mca": "Master of Computer Applications",
    "llb": "Bachelor of Laws", "llm": "Master of Laws",
    "diploma": "Diploma",
}

SKILL_ALIASES = {
    "js": "javascript", "javascript": "javascript",
    "ts": "typescript", "typescript": "typescript",
    "py": "python", "python": "python",
    "reactjs": "react", "react.js": "react", "react": "react",
    "nodejs": "node.js", "node": "node.js", "node.js": "node.js",
    "ml": "machine learning", "machine learning": "machine learning",
    "ai": "artificial intelligence",
    "html5": "html", "css3": "css",
    "postgres": "postgresql", "postgresql": "postgresql",
    "mongo": "mongodb", "mongodb": "mongodb",
    "aws": "amazon web services (aws)",
    "gcp": "google cloud platform (gcp)",
    "k8s": "kubernetes",
    "c++": "c++", "cpp": "c++",
    "csharp": "c#", "c#": "c#",
    "excel": "microsoft excel", "ms excel": "microsoft excel",
    "powerbi": "power bi", "power bi": "power bi",
    "sql": "sql",
}


def normalize_email(raw: str) -> str:
    return raw.strip().lower().rstrip(".,;")


def normalize_url(raw: str) -> str:
    url = raw.strip().rstrip(".,;")
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    return url.lower()


def normalize_phone(raw: str, default_region: str = "US") -> str:
    """Normalize to E.164 (+<countrycode><number>) using `phonenumbers` when
    available; falls back to a best-effort regex cleanup otherwise."""
    try:
        import phonenumbers
        for region in (None, default_region):
            try:
                parsed = phonenumbers.parse(raw, region)
                if phonenumbers.is_valid_number(parsed) or phonenumbers.is_possible_number(parsed):
                    return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
            except phonenumbers.NumberParseException:
                continue
    except ImportError:
        pass

    # Fallback: simple cleanup, no reliable country-code splitting without a library
    digits = re.sub(r"[^\d+]", "", raw).strip()
    if digits.startswith("00"):
        digits = "+" + digits[2:]
    return digits


def normalize_date(month: Optional[str], year: str) -> str:
    """Return 'YYYY-MM' if month known, else 'YYYY'."""
    if month:
        mkey = month.strip(".").lower()[:3]
        # allow full month names too
        mkey_full = month.strip(".").lower()
        mm = MONTHS.get(mkey_full) or MONTHS.get(mkey)
        if mm:
            return f"{year}-{mm}"
    return year


def normalize_degree(raw: str) -> str:
    key = raw.strip().lower().replace(" ", "")
    for k, v in DEGREE_MAP.items():
        if key == k.replace(" ", "").replace(".", "") or key == k.replace(" ", ""):
            return v
    # try direct substring match (e.g. "B.Tech in Computer Science")
    for k, v in DEGREE_MAP.items():
        if k.replace(".", "") in key:
            return v
    return raw.strip()


def normalize_skill(raw: str) -> str:
    key = raw.strip().lower().strip(".,;:")
    return SKILL_ALIASES.get(key, key)


# --------------------------------------------------------------------------
# 3. SECTION SPLITTING
# --------------------------------------------------------------------------

SECTION_HEADERS = {
    "summary": [r"^(professional\s+)?summary$", r"^objective$", r"^profile$", r"^about\s*me$"],
    "experience": [r"^(work\s+|professional\s+)?experience$", r"^employment(\s+history)?$",
                   r"^work\s+history$", r"^career\s+history$"],
    "education": [r"^education(al)?(\s+background|\s+qualifications?)?$", r"^academic(s)?$"],
    "skills": [r"^(technical\s+|key\s+|core\s+)?skills$", r"^skills\s*(&|and)\s*abilities$",
               r"^technical\s+proficienc(y|ies)$", r"^competencies$"],
    "projects": [r"^projects?$", r"^academic\s+projects?$", r"^personal\s+projects?$"],
    "certifications": [r"^certifications?$", r"^certificates?$", r"^licenses?(\s+&\s+certifications)?$"],
    "languages": [r"^languages?$", r"^language\s+proficienc(y|ies)$"],
    "achievements": [r"^achievements?$", r"^awards?(\s+&\s+honors)?$", r"^honors?$"],
    "publications": [r"^publications?$"],
    "references": [r"^references?$"],
}

_HEADER_LOOKUP = [
    (re.compile(pat, re.IGNORECASE), name)
    for name, patterns in SECTION_HEADERS.items()
    for pat in patterns
]


def split_sections(text: str) -> Dict[str, str]:
    """Split resume text into named sections based on common header lines."""
    lines = [l.strip() for l in text.split("\n")]
    sections: Dict[str, List[str]] = {"header": []}
    current = "header"

    for line in lines:
        clean = line.strip().strip(":").strip()
        matched = None
        # A header line is usually short (<=4 words) and matches a known pattern
        if 0 < len(clean.split()) <= 5:
            for pattern, name in _HEADER_LOOKUP:
                if pattern.match(clean):
                    matched = name
                    break
        if matched:
            current = matched
            sections.setdefault(current, [])
            continue
        sections.setdefault(current, [])
        sections[current].append(line)

    return {k: "\n".join(v).strip() for k, v in sections.items()}


# --------------------------------------------------------------------------
# 4. FIELD EXTRACTORS
# --------------------------------------------------------------------------

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}")
PHONE_RE = re.compile(r"(\+?\d[\d\-\s().]{7,}\d)")
LINKEDIN_RE = re.compile(r"(?:https?://)?(?:www\.)?linkedin\.com/[a-zA-Z0-9_/\-]+", re.IGNORECASE)
GITHUB_RE = re.compile(r"(?:https?://)?(?:www\.)?github\.com/[a-zA-Z0-9_/\-]+", re.IGNORECASE)
GENERIC_URL_RE = re.compile(r"(?:https?://)?(?:www\.)?[a-zA-Z0-9\-]+\.[a-zA-Z]{2,}(?:/[^\s|]*)?")


def extract_contact_info(full_text: str) -> Dict[str, Any]:
    contact: Dict[str, Any] = {}

    emails = EMAIL_RE.findall(full_text)
    if emails:
        contact["email"] = normalize_email(emails[0])

    phones = PHONE_RE.findall(full_text)
    if phones:
        # pick the candidate with the most digits (avoids matching zip codes etc.)
        best = max(phones, key=lambda p: len(re.sub(r"\D", "", p)))
        if len(re.sub(r"\D", "", best)) >= 7:
            contact["phone"] = normalize_phone(best)

    li = LINKEDIN_RE.search(full_text)
    if li:
        contact["linkedin"] = normalize_url(li.group(0))

    gh = GITHUB_RE.search(full_text)
    if gh:
        contact["github"] = normalize_url(gh.group(0))

    # Portfolio/personal site: first generic URL that isn't linkedin/github/email
    # Mask out email matches first so a URL regex can't match a fragment of an email.
    text_no_emails = EMAIL_RE.sub(" ", full_text)
    for m in GENERIC_URL_RE.finditer(text_no_emails):
        candidate = m.group(0)
        low = candidate.lower()
        if "linkedin.com" in low or "github.com" in low:
            continue
        if "." in candidate and len(candidate) > 6:
            contact["portfolio"] = normalize_url(candidate)
            break

    # Location: heuristic - look for "City, ST" or "City, Country" pattern near top
    loc_match = re.search(r"\b([A-Z][a-zA-Z\.\s]{2,20},\s?[A-Z][a-zA-Z]{1,20})\b", full_text[:500])
    if loc_match:
        contact["location"] = loc_match.group(1).strip()

    return contact


def extract_name(full_text: str, contact: Dict[str, Any]) -> Optional[str]:
    """Heuristic: the name is usually the first substantive line that isn't
    contact info, a section header, or overly long."""
    for line in full_text.split("\n")[:8]:
        clean = line.strip()
        if not clean:
            continue
        if EMAIL_RE.search(clean) or PHONE_RE.search(clean):
            continue
        if any(k in clean.lower() for k in ["linkedin", "github", "http", "curriculum", "resume", "cv"]):
            continue
        words = clean.split()
        if 1 <= len(words) <= 4 and not any(ch.isdigit() for ch in clean):
            # Looks like a name (short, no digits)
            return clean.title() if clean.isupper() else clean
    return None


DATE_RANGE_RE = re.compile(
    r"(?P<m1>[A-Za-z]{3,9}\.?)?\s*(?P<y1>(19|20)\d{2})\s*(?:[-–—to]+)\s*"
    r"(?P<present>present|current|ongoing|now)|"
    r"(?P<m1b>[A-Za-z]{3,9}\.?)?\s*(?P<y1b>(19|20)\d{2})\s*(?:[-–—]|to)\s*"
    r"(?P<m2b>[A-Za-z]{3,9}\.?)?\s*(?P<y2b>(19|20)\d{2})",
    re.IGNORECASE,
)


def parse_date_range(text: str) -> Optional[Dict[str, str]]:
    m = DATE_RANGE_RE.search(text)
    if not m:
        return None
    gd = m.groupdict()
    if gd.get("present"):
        start = normalize_date(gd.get("m1"), gd["y1"])
        return {"start": start, "end": "Present"}
    if gd.get("y1b") and gd.get("y2b"):
        start = normalize_date(gd.get("m1b"), gd["y1b"])
        end = normalize_date(gd.get("m2b"), gd["y2b"])
        return {"start": start, "end": end}
    return None


def duration_months(start: str, end: str) -> int:
    def to_ym(d):
        if d.lower() == "present":
            now = datetime.now()
            return now.year, now.month
        parts = d.split("-")
        y = int(parts[0])
        mo = int(parts[1]) if len(parts) > 1 else 6  # assume mid-year if month unknown
        return y, mo

    y1, m1 = to_ym(start)
    y2, m2 = to_ym(end)
    return max(0, (y2 - y1) * 12 + (m2 - m1))


def _split_title_company(header_line: str) -> (Optional[str], Optional[str]):
    """Best-effort split of a 'title/company' header line into (title, company)."""
    # Strip an inline date range if the header line also carries the dates
    cleaned = DATE_RANGE_RE.sub("", header_line).strip(" |,-")
    if "|" in cleaned:
        parts = [p.strip() for p in cleaned.split("|") if p.strip()]
        return (parts[0], parts[1] if len(parts) > 1 else None)
    if " at " in cleaned.lower():
        idx = cleaned.lower().index(" at ")
        return cleaned[:idx].strip(), cleaned[idx + 4:].strip()
    if "," in cleaned:
        parts = [p.strip() for p in cleaned.split(",") if p.strip()]
        return parts[0], (parts[1] if len(parts) > 1 else None)
    if " - " in cleaned:
        parts = [p.strip() for p in cleaned.split(" - ") if p.strip()]
        return parts[0], (parts[1] if len(parts) > 1 else None)
    return cleaned or None, None


def extract_experience(section_text: str) -> List[Dict[str, Any]]:
    """Split the experience section into entries.

    Assumes the common resume pattern:
        Job Title | Company        <- header line (or header may share the date line)
        Jan 2021 - Present         <- date line
        - bullet describing work   <- description (belongs to the entry above)
        - another bullet
        Next Job Title | Company   <- next header line
        ...
    Description lines that appear between one date line and the *next*
    header line are attributed to the entry whose date line precedes them.
    """
    if not section_text:
        return []

    lines = [l.strip() for l in section_text.split("\n") if l.strip()]
    date_idxs = [i for i, l in enumerate(lines) if DATE_RANGE_RE.search(l)]
    if not date_idxs:
        return []

    entries: List[Dict[str, Any]] = []
    prev_end = 0  # index where the previous entry's trailing description ends (exclusive)

    for pos, date_idx in enumerate(date_idxs):
        # The header is normally the line immediately before the date line;
        # if the date itself is embedded in that same line, header_idx == date_idx.
        header_idx = date_idx if DATE_RANGE_RE.search(lines[date_idx]) and (
            date_idx == 0 or not lines[date_idx - 1].strip()
        ) else max(prev_end, date_idx - 1)

        # Anything between prev_end and header_idx is trailing description of the PREVIOUS entry
        if entries and header_idx > prev_end:
            trailing = lines[prev_end:header_idx]
            if trailing:
                entries[-1]["description"] = (
                    (entries[-1]["description"] + "\n" + "\n".join(trailing)).strip()
                )

        header_line = lines[header_idx]
        dates = parse_date_range(lines[date_idx])
        title, company = _split_title_company(header_line)

        entries.append({
            "title": title,
            "company": company,
            "start_date": dates["start"] if dates else None,
            "end_date": dates["end"] if dates else None,
            "duration_months": duration_months(dates["start"], dates["end"]) if dates else None,
            "description": "",
        })

        # Description for THIS entry starts right after the date line, and runs
        # until the header of the next entry (handled at top of next loop iteration)
        if pos + 1 < len(date_idxs):
            next_date_idx = date_idxs[pos + 1]
            next_header_idx = max(date_idx + 1, next_date_idx - 1)
        else:
            next_header_idx = len(lines)  # last entry: everything remaining is its description
        desc_lines = lines[date_idx + 1:next_header_idx]
        if desc_lines:
            entries[-1]["description"] = "\n".join(desc_lines).strip()
        prev_end = next_header_idx

    return entries


def extract_education(section_text: str) -> List[Dict[str, Any]]:
    if not section_text:
        return []
    lines = [l for l in section_text.split("\n") if l.strip()]
    entries = []
    current_block: List[str] = []

    def flush(block: List[str]):
        if not block:
            return
        block_text = "\n".join(block)
        year_match = re.search(r"(19|20)\d{2}", block_text)
        year = year_match.group(0) if year_match else None

        degree_match = None
        for key in DEGREE_MAP:
            if re.search(r"\b" + re.escape(key).replace(r"\.", r"\.?") + r"\b", block_text, re.IGNORECASE):
                degree_match = key
                break
        degree = normalize_degree(degree_match) if degree_match else None

        institution = None
        for line in block:
            if re.search(r"(university|college|institute|school|academy|polytechnic)", line, re.IGNORECASE):
                institution = line.strip()
                break

        entries.append({
            "degree": degree,
            "institution": institution,
            "year": year,
            "raw": block_text.strip(),
        })

    def block_has_year(block: List[str]) -> bool:
        return any(re.search(r"(19|20)\d{2}", l) for l in block)

    for line in lines:
        has_year = re.search(r"(19|20)\d{2}", line)
        institution_line = re.search(r"(university|college|institute|school|academy|polytechnic)", line, re.IGNORECASE)
        # Start a new entry only once the current block already looks "complete"
        # (already has a year) and we see the start of another entry.
        if current_block and block_has_year(current_block) and (has_year or institution_line):
            flush(current_block)
            current_block = [line]
        else:
            current_block.append(line)
    if current_block:
        flush(current_block)
    return entries


def extract_skills(section_text: str) -> List[str]:
    if not section_text:
        return []
    # Split on common delimiters: commas, bullets, pipes, semicolons, newlines
    raw_tokens = re.split(r"[,\n|;•·▪●\u2022]+", section_text)
    skills = []
    seen = set()
    for tok in raw_tokens:
        tok = tok.strip(" -\t")
        if not tok or len(tok) > 40:  # skip empty / accidental long sentences
            continue
        norm = normalize_skill(tok)
        if norm and norm not in seen:
            seen.add(norm)
            skills.append(norm)
    return skills


def extract_list_section(section_text: str) -> List[str]:
    """Generic splitter for certifications/languages/achievements sections."""
    if not section_text:
        return []
    items = re.split(r"[\n•·▪●\u2022]+", section_text)
    return [i.strip(" -\t") for i in items if i.strip()]


def compute_total_experience(experience: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Sum experience durations (does not merge overlapping ranges)."""
    total_months = sum(e["duration_months"] for e in experience if e.get("duration_months"))
    years = total_months // 12
    months = total_months % 12
    return {"total_months": total_months, "years": years, "months": months,
            "formatted": f"{years} years, {months} months"}


# --------------------------------------------------------------------------
# 5. MAIN PARSER
# --------------------------------------------------------------------------

@dataclass
class ResumeData:
    file: str
    name: Optional[str] = None
    contact: Dict[str, Any] = field(default_factory=dict)
    summary: Optional[str] = None
    skills: List[str] = field(default_factory=list)
    experience: List[Dict[str, Any]] = field(default_factory=list)
    education: List[Dict[str, Any]] = field(default_factory=list)
    certifications: List[str] = field(default_factory=list)
    projects: List[str] = field(default_factory=list)
    languages: List[str] = field(default_factory=list)
    achievements: List[str] = field(default_factory=list)
    total_experience: Dict[str, Any] = field(default_factory=dict)

    def to_json(self, indent=2) -> str:
        return json.dumps(asdict(self), indent=indent, ensure_ascii=False)


def parse_resume(path: str) -> ResumeData:
    raw_text = extract_text(path)
    sections = split_sections(raw_text)

    contact = extract_contact_info(raw_text)
    name = extract_name(sections.get("header", raw_text), contact)
    experience = extract_experience(sections.get("experience", ""))
    education = extract_education(sections.get("education", ""))
    skills = extract_skills(sections.get("skills", ""))

    data = ResumeData(
        file=str(path),
        name=name,
        contact=contact,
        summary=sections.get("summary", "").strip() or None,
        skills=skills,
        experience=experience,
        education=education,
        certifications=extract_list_section(sections.get("certifications", "")),
        projects=extract_list_section(sections.get("projects", "")),
        languages=extract_list_section(sections.get("languages", "")),
        achievements=extract_list_section(sections.get("achievements", "")),
        total_experience=compute_total_experience(experience),
    )
    return data


# --------------------------------------------------------------------------
# 6. CLI
# --------------------------------------------------------------------------

def main():
    # parser = argparse.ArgumentParser(description="Detailed resume analyzer (PDF/DOCX).")
    # parser.add_argument("resume", help="Path to the resume file (.pdf or .docx)")
    # parser.add_argument("--out", help="Path to write JSON output", default=None)
    # args = parser.parse_args()

    result = parse_resume(r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Knowledge Graph\resumes\SanjeetSahasrabudheResume.docx")
    output_json = result.to_json()

    Path(r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Knowledge Graph\out\output_sanjeet.json").write_text(output_json, encoding="utf-8")
    print(f"Saved structured output to")


if __name__ == "__main__":
    main()
