import csv
import re
import unicodedata
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# path= r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Process\leveled.csv"

# df=pd.read_csv(path)

def _normalize_company(df):

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

    def normalize_company(company):
        company = company.lower()
        company = clean_domain(company)
        company = remove_suffix(company)
        company=  clean_text(company)
        if company in abbrDict:
            company=abbrDict[company]
        return company



    abbrDict = {
        "tcs": "tata consultancy services",
        "ibm": "international business machines",
        "infosys ltd": "infosys",
    }


    cnt=0
    coList=[]
    newRows = []
    for i,row in df.iterrows():
        # print(i,row)
        Company = str(row['Company'])
        # print(f"before_{Company}")
        updated_company = normalize_company(Company)
        # print(f"after_{updated_company}")
        newrow = row.copy()
        newrow['Updated_Company'] = updated_company
        newRows.append(newrow)

    newDf = pd.DataFrame(newRows)

    updated_company_Col = newDf.pop('Updated_Company')

    companyIndex = newDf.columns.get_loc('Company')

    newDf.insert(companyIndex + 1, 'Updated_Company', updated_company_Col)

    newDf.to_csv("Company_Noralized.csv")

    return newDf
