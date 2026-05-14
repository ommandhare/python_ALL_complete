import re
import unicodedata
import spacy
import pandas as pd

path=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Word Count.csv"


# nlp = spacy.load("en_core_web_sm")

variant_dict = {
    "jr.": "jr",

    # Manager
    "mngr": "mgr",
    "mgmt": "management",
    "mgmts": "management",

    # Engineering
    "engg": "eng",
    "engr": "eng",
    "engr.": "eng",
    "engrs": "engineers",

    # Developer
    "devloper": "developer",
    "devlpr": "developer",
    "devs": "developers",

    # Analyst
    "analysts": "analyst",
    "analist": "analyst",
    "analysist": "analyst",

    # Admin
    "admins": "admin",
    "administrators": "administrator",

    # Consultant
    "consulting": "consultant",
    "consults": "consultant",

    # HR
    "hrs": "hr",

    # Finance
    "fins": "finance",
    "accts": "accounting",

    # Plurals
    "engineers": "engineer",
    "developers": "developer",
    "managers": "manager",
    "architects": "architect",
    "designers": "designer",
    "scientists": "scientist",
    "specialists": "specialist"
}

stop_words = {
    "and",
    "or",
    "of",
    "the",
    "for",
    "to",
    "in",
    "on",
    "with",
    "at",
    "from",
    "by",
    "via",
    "a",
    "an",
    "as",
    "into",
    "within",
    "across",
    "over",
    "under",
    "department",
    "dept",
    "division",
    "team",
    "unit",
    "services",
    "solutions",
    "systems",
    "operations",
    "global",
    "regional",
    "corporate",
    "enterprise",
    "international",
    "india",
    "usa",
    "uk"
}

abbreviation_dict =  {

    # -----------------------------------------------------
    # EXECUTIVE ROLES
    # -----------------------------------------------------

    "ceo": "chief executive officer",
    "cto": "chief technology officer",
    "cfo": "chief financial officer",
    "cio": "chief information officer",
    "coo": "chief operating officer",
    "cmo": "chief marketing officer",
    "cdo": "chief data officer",
    "cro": "chief revenue officer",
    "cso": "chief strategy officer",
    "chro": "chief human resources officer",


    # -----------------------------------------------------
    # SENIORITY
    # -----------------------------------------------------

    "sr": "senior",
    "jr": "junior",
    "assoc": "associate",
    "asst": "assistant",
    "lead": "lead",
    "prin": "principal",


    # -----------------------------------------------------
    # MANAGEMENT
    # -----------------------------------------------------

    "mgr": "manager",
    "dir": "director",
    "vp": "vice president",
    "avp": "assistant vice president",
    "svp": "senior vice president",
    "evp": "executive vice president",
    "gm": "general manager",


    # -----------------------------------------------------
    # SOFTWARE / TECH
    # -----------------------------------------------------

    "sde": "software development engineer",
    "swe": "software engineer",
    "dev": "developer",
    "eng": "engineer",
    "qa": "quality assurance",
    "qc": "quality control",
    "ui": "user interface",
    "ux": "user experience",
    "db": "database",
    "dba": "database administrator",
    "etl": "extract transform load",
    "bi": "business intelligence",
    "ai": "artificial intelligence",
    "ml": "machine learning",
    "dl": "deep learning",
    "nlp": "natural language processing",
    "cv": "computer vision",
    "ds": "data science",
    "de": "data engineer",
    "da": "data analyst",
    "ba": "business analyst",
    "pm": "project manager",
    "po": "product owner",
    "sm": "scrum master",
    "devops": "development operations",
    "secops": "security operations",
    "it": "information technology",


    # -----------------------------------------------------
    # HR
    # -----------------------------------------------------

    "hr": "human resources",
    "ta": "talent acquisition",
    "lnd": "learning and development",
    "l&d": "learning and development",
    "recruiter": "recruitment",


    # -----------------------------------------------------
    # FINANCE
    # -----------------------------------------------------

    "acct": "accounting",
    "fin": "finance",
    "fp&a": "financial planning and analysis",
    "ca": "chartered accountant",
    "cpa": "certified public accountant",


    # -----------------------------------------------------
    # SALES / MARKETING
    # -----------------------------------------------------

    "bd": "business development",
    "bde": "business development executive",
    "seo": "search engine optimization",
    "sem": "search engine marketing",
    "smm": "social media marketing",
    "crm": "customer relationship management",


    # -----------------------------------------------------
    # SUPPORT / OPERATIONS
    # -----------------------------------------------------

    "ops": "operations",
    "admin": "administrator",
    "cust": "customer",
    "cs": "customer support",
    "cx": "customer experience",
    "scm": "supply chain management",
    "log": "logistics"
}

base_word_dict = {
    "development": "develop",
    "developing": "develop",

    # Analysis
    "analytics": "analysis",
    "analyst": "analysis",
    "analysts": "analysis",

    # Management
    "management": "manage",
    "manager": "manage",
    "managers": "manage",
    "managing": "manage",

    # Consulting
    "consultant": "consult",
    "consulting": "consult",

    # Design
    "designer": "design",
    "designing": "design",
    "designers": "design",

    # Architecture
    "architect": "architecture",
    "architects": "architecture",

    # Operations
    "operations": "operation",
    "operational": "operation",

    # Administration
    "administrator": "admin",
    "administration": "admin",

    # Science
    "scientist": "science",
    "scientists": "science",

    # Finance
    "financial": "finance",
    "financing": "finance",

    # Marketing
    "marketing": "market",
    "marketer": "market",

    # Recruitment
    "recruitment": "recruit",
    "recruiter": "recruit"
}


def clean_text(txt):
    txt = str(txt)

    txt = txt.lower()

    # Remove corrupted UTF patterns
    txt = re.sub(r'â\S*', ' ', txt)

    # Normalize unicode
    txt = unicodedata.normalize('NFKD', txt)

    # Convert accented chars to ASCII
    txt = txt.encode('ascii', 'ignore').decode('utf-8')

    # Replace &
    txt = txt.replace("&", "and")

    # Keep only letters/numbers/spaces
    txt = re.sub(r'[^A-Za-z ]', '', txt)

    # Remove extra spaces
    txt = " ".join(txt.split())

    return txt

cleanWordLst=[]
baseWordLst=[]

for line in open(path):
    word,count=line.strip().split(",")
    if word=="":
        continue
    word=clean_text(word)
    cleanWordLst.append(word)

print(cleanWordLst)

baseDict={}
print("variant changing... e.g engr ---> engg")
for word in cleanWordLst:
    if word in variant_dict:
        # print("before  ",word)
        baseword =variant_dict[word]
        baseDict[word] = baseword
        baseWordLst.append(baseword)
        # print("After  ", word)
    # if word in stop_words:
        # print(word ,"ignored stop word")
        # word = "--"
    elif word in abbreviation_dict:
        # print("before",word)
        baseword = abbreviation_dict[word]
        baseDict[word] = baseword
        baseWordLst.append(baseword)
        # print("After",word)
    elif word in base_word_dict:
        # print("before",word)
        baseword = base_word_dict[word]
        baseDict[word] = baseword
        baseWordLst.append(baseword)
        # print("After",word)
    else:
        baseDict[word] = word
        baseWordLst.append(word)


print(baseWordLst)
print(baseDict)


df = pd.DataFrame(list(baseDict.items()), columns=['word', 'base_word'])

df.to_csv("base_word_dict.csv")
