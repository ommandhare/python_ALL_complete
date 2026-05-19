import re
import unicodedata
import pandas as pd

path=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Word Count.csv"


variant_dict = {
    "jr.": "jr",

    # Manager
    "mngr": "mgr",
    "mgt" : "management",
    "mgmt": "management",
    "mgmts": "management",

    # Engineering
    "engg": "engg",
    "engr": "engg",
    "engr.": "engg",
    "engrs": "engineers",

    # Developer
    "devloper": "developer",
    "devlpr": "developer",
    "devs": "developer",
    "exp": "Experience",
    "Gra": "Graduate",

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
    "consltancy": "consultancy",

    # HR
    "hrs": "hr",
    "yrs":"years",

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
    "specialists": "specialist",
    "sottware": "software"
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
    "under"
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
    "uk": "united kingdom",



    # -----------------------------------------------------
    # MANAGEMENT
    # -----------------------------------------------------

    "mgr": "manager",
    "dir": "director",
    "vp": "vice president",
    "avp": "assistant vice president",
    "svp": "senior vice president",
    "evp": "executive vice president",
    "rvp": "regional vice president",
    "gm": "general manager",
    "pmo":"project management office",
    "agm": "assistant general manager",
    "dgm":"deputy general manager",
    "md": "managing director",
    "randd":"research and Development",
    "iiot":"industrial internet of things",
    "sez":"special economic zone",
    "csr":"corpoarte social responsibility",


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
    "dy":"deputy",
    "sre":"site reliability engg",
    "pvt":"private",
    "ltd":"limited",
    "e4r":"engg for research",
    "irc":"informartion and research center",
    "grc":"governance risk compliance",
    "gcp":"google cloud platform",
    "mom":"manufacturing operation management",
    "apm":"application performance monitoring",
    "cae":"computer aided design",
    "acm":"active category management",
    "eam":"enterprise asset management",
    "mis":"management information system",
    "tug":"tableu user group",
    "exb":"engineering excellence bureau",
    "gbs":"global business services",
    "npd":"new product development",
    "asc":"Associate",
    "ind":"india",
    "gra":"graduate",


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
    "log": "logistics",
    "iot": "Internet of Things",
    "cw": "Contract Worker"
}

base_word_dict = {

    # Analysis
    "analytics": "analytics",
    "analyst": "analyst",
    "analysts": "analyst",

    # Management
    "management": "management",
    "manager": "manager",
    "managers": "manager",
    "managing": "manager",

    # Consulting
    "consulting": "consultant",

    # Design
    "designing": "design",
    "designers": "design",

    "operational": "operation",

    # Administration
    "administrator": "admin",
    "administration": "admin",

    "scientists": "scientist",

    # Finance
    "financial": "finance",
    "financing": "finance",

    # Marketing
    "marketing": "market",
    "marketer": "market",

    # Recruitment
    "recruitment": "recruiter",
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
