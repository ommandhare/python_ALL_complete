import re
import pdfplumber
from docx import Document
import dateparser
import json

##########################################################################
# READ RESUME
##########################################################################

def read_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text

def read_docx(file_path):
    doc = Document(file_path)

    text = ""

    for para in doc.paragraphs:
        text += para.text + "\n"

    return text

def read_resume(file_path):

    if file_path.lower().endswith(".pdf"):
        return read_pdf(file_path)

    elif file_path.lower().endswith(".docx"):
        return read_docx(file_path)

    else:
        raise Exception("Unsupported Format")

def extract_email(text):

    pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    match = re.search(pattern, text)

    return match.group() if match else ""

def extract_phone(text):

    pattern = r'(\+?\d[\d\s\-]{8,15}\d)'

    match = re.search(pattern, text)

    return match.group() if match else ""

def extract_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) > 2:

            if "resume" not in line.lower():

                return line

    return ""

SECTION_HEADERS = [
    "summary",
    "professional summary",
    "experience",
    "work experience",
    "employment",
    "skills",
    "technical skills",
    "projects",
    "project",
    "education",
    "certification",
    "certifications",
    "training",
    "languages",
    "verbal languages skills"
    "personal details",
    "declaration",

    # Add these
    "name of the project",
    "role",
    "company",
    "client",
    "technology",
    "roles and responsibilities",
    "date"
]

def extract_section(text, section_name):

    pattern = rf"{section_name}(.*?)(?=\n(?:{'|'.join(SECTION_HEADERS)})\b|\Z)"

    match = re.search(
        pattern,
        text,
        re.I | re.S
    )

    if match:
        return match.group(1).strip()

    return ""

def extract_summary(text):

    headers = [
        "professional summary",
        "summary",
        "profile",
        "career summary"
    ]

    for h in headers:

        data = extract_section(text, h)

        if data:
            return data

    return ""

SKILLS = {

"Programming Languages":[
"Python","Java","C","C++","SQL"
],

"Big Data":[
"Spark",
"Hadoop",
"Hive",
"Kafka"
],

"Cloud":[
"GCP",
"Azure",
"AWS",
"BigQuery",
"Databricks"
],

"Visualization":[
"Power BI",
"Tableau",
"Dash",
"Plotly",
"Excel"
],

"Machine Learning":[
"Scikit",
"TensorFlow",
"PyTorch",
"XGBoost"
],

"Database":[
"MySQL",
"Oracle",
"MongoDB",
"PostgreSQL"
]

}

def extract_skills(text):


    result={}

    lower=text.lower()

    for category,skills in SKILLS.items():

        found=[]

        for skill in skills:

            if skill.lower() in lower:
                found.append(skill)

        result[category]=found

    return result

def extract_experience(text):

    section = extract_section(text, "work experience")

    if not section:
        section = extract_section(text, "experience")

    return section

def extract_date_ranges(text):
    pattern = r'([A-Za-z]{3,9}[- ]?\d{4})\s*(?:-|–|to)\s*(Present|Current|[A-Za-z]{3,9}[- ]?\d{4})'

    return re.findall(pattern, text)

def extract_companies(text):

    pattern = r'(?:Company|Employer|Organization)\s*:\s*(.*)'

    return re.findall(pattern, text)

def extract_clients(text):

    pattern = r'Client\s*:\s*(.*)'

    return re.findall(pattern, text)

def extract_projects(text):

    pattern = r'Project\s*:\s*(.*)'

    return re.findall(pattern, text)


def extract_value(block, labels, multiline=False):
    """
    Extract value for one or more possible labels.
    """

    if isinstance(labels, str):
        labels = [labels]

    for label in labels:

        if multiline:
            pattern = rf'{label}\s*:\s*(.*?)(?=\n(?:Name\s+of\s+the\s+Project|Project|Role|Company|Client|Date|Technology|Data Source|Education|Certifications|Declaration|$))'
        else:
            pattern = rf'{label}\s*:\s*(.+)'

        match = re.search(pattern, block, re.I | re.S)

        if match:
            return match.group(1).strip()

    return ""

def parse_experience(block):

    experience = {}

    experience["Project"] = extract_value(
        block,
        ["Name of the Project", "Project", "Project Name"]
    )

    experience["Role"] = extract_value(
        block,
        ["Role", "Designation", "Title"]
    )

    experience["Company"] = extract_value(
        block,
        ["Company", "Employer"]
    )

    experience["Client"] = extract_value(
        block,
        ["Client"]
    )

    experience["Timeline"] = extract_value(
        block,
        ["Date", "Duration", "Timeline"]
    )

    experience["Technology Used"] = extract_value(
        block,
        ["Technology", "Technology Stack", "Tech Stack", "Tools"]
    )

    experience["Work Summary"] = extract_value(
        block,
        ["Roles and Responsibilities", "Responsibilities", "Job Description"],
        multiline=True
    )

    return experience

import re

def split_work_experience(work_text):
    """
    Returns one block per project.
    """

    # Match the start of every project
    pattern = r'(?i)^Name\s+of\s+the\s+Project\s*:'

    matches = list(re.finditer(pattern, work_text, re.MULTILINE))

    if not matches:
        return []

    blocks = []

    for i in range(len(matches)):

        start = matches[i].start()

        if i == len(matches) - 1:
            end = len(work_text)
        else:
            end = matches[i + 1].start()

        block = work_text[start:end].strip()

        blocks.append(block)

    return blocks

def parse_all_experiences(text):

    blocks = split_work_experience(text)

    experiences = []

    for block in blocks:
        exp = parse_experience(block)

        # Ignore empty blocks
        if exp["Project"] or exp["Role"] or exp["Company"]:
            experiences.append(exp)

    return experiences

def get_value(block, field):
    import re

    FIELDS = [
        "Name of the Project",
        "Project",
        "Role",
        "Company",
        "Client",
        "Date",
        "Timeline",
        "Technology",
        "Technology Stack",
        "Roles and Responsibility",
        "Roles and Responsibilities",
        "Responsibilities"
    ]

# def extract_field(block, field):
#         # Every other field acts as a stopping point
#
#         stop = "|".join(re.escape(f) for f in FIELDS)
#
#         pattern = rf"""
#             {re.escape(field)}\s*:\s*      # Current field
#             (.*?)                          # Capture lazily
#             (?=\n(?:{stop})\s*:|\Z)         # Stop at next field or end
#         """
#
#         match = re.search(pattern, block, re.I | re.S | re.X)
#
#         if match:
#             return match.group(1).strip()
#
#         return ""

FIELDS = {
    "name of the project": "Project",
    "project name": "Project",
    "role": "Role",
    "designation": "Role",
    "company": "Company",
    "client": "Client",
    "date": "Timeline",
    "duration": "Timeline",
    "technology": "Technology Used",
    "technology stack": "Technology Used",
    "roles and responsibility": "Work Summary",
    "roles and responsibilities": "Work Summary",
    "responsibilities": "Work Summary"
}

def parse_project(block):

    result = {
        "Project": "",
        "Role": "",
        "Company": "",
        "Client": "",
        "Timeline": "",
        "Technology Used": "",
        "Work Summary": ""
    }


    field_patterns = {

        "Project": r"^(Name of the Project|Project Name)\s*:",

        "Role": r"^Role\s*:",

        "Company": r"^Company\s*:",

        "Client": r"^Client\s*:",

        "Timeline": r"^(Date|Timeline|Duration)\s*:",

        "Technology Used": r"^(Technology|Technology Stack|Tech Stack)\s*:",

        "Work Summary": r"^(Roles and Responsibility|Roles and Responsibilities|Responsibilities)\s*:"

    }


    current = None


    for line in block.splitlines():

        line = line.strip()


        if not line:
            continue


        matched = False


        for field, pattern in field_patterns.items():

            if re.match(pattern, line, re.I):

                current = field

                result[field] = line.split(":",1)[1].strip()

                matched = True

                break


        if not matched and current:

            result[current] += "\n" + line


    return result

def extract_roles(text):

    pattern = r'(?:Role|Designation|Title)\s*:\s*(.*)'

    return re.findall(pattern, text)

def extract_responsibilities(text):

    lines=[]

    for line in text.split("\n"):

        line=line.strip()

        if len(line)<15:
            continue

        if re.match(r'^(Developed|Designed|Built|Created|Implemented|Worked|Managed|Performed|Processed|Engineered)',line,re.I):
            lines.append(line)

    return lines

def extract_education(text):

    return extract_section(text, "education")

def extract_certifications(text):

    data = extract_section(text, "certifications")

    if not data:

        data = extract_section(text, "training")

    return data

def extract_personal_details(text):

    return extract_section(text, "personal details")

def extract_declaration(text):

    return extract_section(text, "declaration")

def extract_languages(text):

    data = extract_section(text, "languages")
    if data=="":
        data = extract_section(text, "verbal language skills")
    return data

def parse_resume(file_path):

    text = read_resume(file_path)

    result = {}
    split_work_exp={}

    result["Name"] = extract_name(text)
    result["Email"] = extract_email(text)
    result["Phone"] = extract_phone(text)

    result["Professional Summary"] = extract_summary(text)

    result["Technical Skills"] = extract_skills(text)

    # result["Work Experience"] = extract_experience(text)

    result["Projects"] = extract_projects(text)

    result["Roles"] = extract_roles(text)

    result["Companies"] = extract_companies(text)

    result["Clients"] = extract_clients(text)

    result["Date Ranges"] = extract_date_ranges(text)

    result["Responsibilities"] = extract_responsibilities(text)

    result["Education"] = extract_education(text)

    result["Certifications"] = extract_certifications(text)

    result["Languages"] = extract_languages(text)

    result["Personal Details"] = extract_personal_details(text)

    result["Declaration"] = extract_declaration(text)

    blocks = split_work_experience(text)
    #
    experiences = []
    #
    for block in blocks:
        experiences.append(parse_project(block))
    #
    split_work_exp["Work Experience"] = experiences

    return result

def parse_resume_split(file_path):

    text = read_resume(file_path)

    split_work_exp={}

    blocks = split_work_experience(text)
    #
    experiences = []
    #
    for block in blocks:
        experiences.append(parse_project(block))
    #
    split_work_exp["Work Experience"] = experiences

    return split_work_exp



def save_json(data, filename):

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )

    print(f"{filename} created successfully")




from pprint import pprint
resume = parse_resume(r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Knowledge Graph\resumes\SanjeetSahasrabudheResume.docx")

Splitwork = parse_resume_split(r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Knowledge Graph\resumes\SanjeetSahasrabudheResume.docx")

# print(resume)
# for k, v in resume.items():
#      print("="*60)
#      pprint(k)
#      pprint(v,width=150)
print(resume)


with open("Resume.json", "w", encoding="utf-8") as file:
    json.dump(
        resume,
        file,
        indent=4,
        ensure_ascii=False
    )

with open("SplitWork.json", "w", encoding="utf-8") as file:

    json.dump(
        Splitwork,
        file,
        indent=4,
        ensure_ascii=False
    )


print("Both JSON files created")




































































# text = read_resume(r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Knowledge Graph\resumes\OmMandhareResume.docx")
# projects = parse_projects(text)

# from pprint import pprint


# pprint(projects)
