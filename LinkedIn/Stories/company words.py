import csv
import re
import unicodedata
import pandas as pd

path= r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Process_sql\Final_flat_table.csv"

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
    "pvtltd"
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

df=pd.read_csv(path)
cnt=0
coList=[]
coDict={}

coList=list(df["Updated_Company"])
# print(coList)
# with open(path, newline='', encoding='utf-8') as file:
#     reader = csv.reader(file)
#
for Company in coList:
#         if freq == 0:
#             freq += 1
#             continue
#
#         First_Name,Last_Name,URL,Email_Address,Company,Updated_Company,Position,Base_Role,Seniority,Connected_On,Owner = line
    Company=clean_text(Company)
    # print(Company)
    Company=remove_suffix(Company)
    # print(Company)
    Company=Company.split(" ")
    for word in Company:
        # print(word)
        if word not in coDict:
            coDict[word] = 1
        else:
            coDict[word] += 1

print(coDict)
df = pd.DataFrame(
    list(coDict.items()),
    columns=['Company_word', 'Count']
)

df = df.sort_values(by='Count', ascending=False)
df.to_csv("Company word Separated.csv")