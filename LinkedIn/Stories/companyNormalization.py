import csv
import re
import unicodedata

path= r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Stories\connections.csv"

suffixes = [
    'pvt',
    'private',
    'ltd',
    'ltd.',
    'limited',
    'llc',
    'inc',
    'inc.',
    '.in',
    'www.',
    'corporation',
    'corp',
    'technologies',
    'technology',
    'co',
    "co.",
]

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


def clean_domain(company):

    company = company.lower().strip()

    # remove protocol
    company = re.sub(r'https?://', '', company)

    # remove www
    company = re.sub(r'^www\.', '', company)

    # keep only first domain part
    company = company.split('.')[0]

    return company



def remove_suffix(company):

    words = company.split()

    clean_words = []

    for w in words:
        if w not in suffixes:
            clean_words.append(w)

    return " ".join(clean_words)

abbrDict = {
    "tcs": "tata consultancy services",
    "ibm": "international business machines",
    "infosys ltd": "infosys",
}


cnt=0
coList=[]
with open(path, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)

    for line in reader:
        if cnt == 0:
            cnt += 1
            continue

        First_Name, Last_Name, URL, Email_Address, Company, Position, Connected_On = line
        coList.append(Company)


# print(coList)


for company in coList:
    company=company.lower()
    company = clean_domain(company)
    company = remove_suffix(company)
    company=clean_text(company)
    if company in abbrDict:
        company=abbrDict[company]

    # if company in c
    print(company)