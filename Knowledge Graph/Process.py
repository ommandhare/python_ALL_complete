import pdfplumber
from docx import Document
import re
import spacy
import pandas as pd
import os
# from parser import extract_text
# from extractor import *
# from matcher import *
# from scoring import ats_score

def extract_text(file):

    if file.endswith(".pdf"):

        text=""

        with pdfplumber.open(file) as pdf:

            for page in pdf.pages:

                text+=page.extract_text()+" "

        return text

    elif file.endswith(".docx"):

        doc=Document(file)

        return "\n".join([p.text for p in doc.paragraphs])

    else:

        return ""


nlp=spacy.load("en_core_web_sm")

def extract_email(text):

    pattern=r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    m=re.search(pattern,text)

    if m:
        return m.group()

    return None


def extract_phone(text):

    pattern=r'(\+91[- ]?)?[6-9]\d{9}'

    m=re.search(pattern,text)

    if m:
        return m.group()

    return None


def extract_name(text):

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    for line in lines[:5]:

        # Ignore long lines
        if len(line.split()) > 4:
            continue

        # Ignore emails
        if "@" in line:
            continue

        # Ignore numbers
        if re.search(r"\d", line):
            continue

        # Ignore common resume headings
        ignore = [
            "resume",
            "curriculum vitae",
            "profile",
            "summary",
            "objective",
            "experience",
            "education",
            "skills"
        ]

        if line.lower() in ignore:
            continue

        return line.title()

    return None


skills_df=pd.read_csv(r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Knowledge Graph\datasets\skills_dataset.csv")

roles_df=pd.read_csv(r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Knowledge Graph\datasets\resume_roles_dataset.csv")


def extract_skills(text):

    text = text.lower()

    skills = set()

    for _, row in skills_df.iterrows():

        skill = str(row["Skill"]).lower().strip()

        # Escape special characters like C++, C#, .NET
        pattern = r'(?<!\w)' + re.escape(skill) + r'(?!\w)'

        if re.search(pattern, text):
            skills.add(row["Skill"])

    return sorted(skills)

def extract_role(text):

    text=text.lower()

    found=[]

    for _,row in roles_df.iterrows():

        role=row["Job_Title"]

        if role.lower() in text:

            found.append(role)

    if len(found):

        return found[0]

    return None

# def ats_score(skills):
#
#     score=0
#
#     score+=len(skills)*5
#
#     if score>100:
#
#         score=100
#
#     return score


folder="resumes"

results=[]

for file in os.listdir(folder):

    path=os.path.join(folder,file)
    print(path)
    text=extract_text(path)
    # print(text)
    name=extract_name(text)
    print(name)
    email=extract_email(text)

    phone=extract_phone(text)

    role=extract_role(text)

    skills=extract_skills(text)
    print(skills)

    # score=ats_score(skills)

    results.append({

        "Resume":file,

        "Name":name,

        "Email":email,

        "Phone":phone,

        "Current Role":role,

        "Skills":", ".join(skills),

        # "ATS Score":score

    })

df=pd.DataFrame(results)

df.to_csv("output/result.csv",index=False)

print(df)
