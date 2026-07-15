import csv
import pandas as pd
import re

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# path=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Stories\Updated Connection.csv"
# freq=0

def get_levels(df):

    levelDict = {

        # Internship
        "Intern": "Internship",
        "Apprentice": "Internship",

        # Entry
        "Associate": "Entry",
        "Analyst": "Entry",
        "Trainee": "Entry",
        "Assistant": "Entry",

        # Junior
        "Junior": "Junior",
        "Jr": "Junior",

        # Mid
        "Engineer": "Mid",
        "Developer": "Mid",
        "Consultant": "Mid",
        "Specialist": "Mid",
        "QA/QC" : "Mid",
        "Clerk" : "Mid",
        "clerk" : "Mid",
        "Data Scientist" : "Mid",
        "Development": "Mid",


        # Senior
        "Senior": "Senior",
        "Sr": "Senior",

        # Lead
        "Lead": "Lead",
        "Team Lead": "Lead",
        "Leader": "Lead",

        # Staff
        "Staff": "Staff",
        "Principal": "Staff",
        "Architect": "Staff",
        "Human Resources" : "HR",
        "HR" : "HR",



        # Management
        "Manager": "Manager",
        "Management":"Manager",
        "Head": "Manager",

        # Senior Management
        "Senior Manager": "Senior_Manager",

        # Director
        "Director": "Director",
        "Senior Director": "Senior_Director",

        # VP
        "VP": "Vice_President",
        "AVP": "Vice_President",
        "SVP": "Vice_President",
        "Vice President": "Vice_President",
        "President" : "President",

        # Executive
        "CEO": "Executive",
        "CTO": "Executive",
        "CFO": "Executive",
        "COO": "Executive",
        "CIO": "Executive",
        "CMO": "Executive",
        "Chief": "Executive",
        "Executive": "Executive",

        # Founder
        "Founder": "Founder",
        "Co-Founder": "Founder",
        "Co Founder": "Founder",

        # Owner
        "Owner": "Owner",
        "Proprietor": "Owner",

        # Partner
        "Partner": "Partner",

        # Advisory
        "Advisor": "Advisor",
        "Mentor": "Advisor",
        "Council" :"Advisor",

        # Academic
        "Professor": "Academic",
        "Researcher": "Academic",

        # Freelance
        "Freelancer": "Freelancer",
        "Independent": "Freelancer",
        "Recruiter" : "Recruiter",
        "Recruitment" : "Recruiter",
        "Admin":"Admin",
        "Administrator":"Admin",
        "self Employed": "Self Employed",
        "Self Employed": "Self Employed",
        "Retired" : "Retired",
        "retired" : "Retired",


    }

    # Sort longest keywords first
    sorted_levels = sorted(
        levelDict.items(),
        key=lambda x: len(x[0]),
        reverse=True
    )

    def extract_levels(position):

        if pd.isna(position):
            return []

        position = str(position)

        found_levels = []

        for keyword, level in sorted_levels:

            # Match whole words/phrases only
            pattern = r'\b' + re.escape(keyword) + r'\b'

            if re.search(pattern, position, flags=re.IGNORECASE):

                found_levels.append(level)

        return list(dict.fromkeys(found_levels))


    # df=pd.read_csv(path)

    seniorityList = []

    newRows = []

    for i, row in df.iterrows():

        position = str(row['Position'])

        levels = extract_levels(position)

        if len(levels) == 0:
            levels = ["Unknown"]

        for level in levels:

            newRow = row.copy()

            newRow['Seniority'] = level

            newRows.append(newRow)


    newDf = pd.DataFrame(newRows)

    seniorityCol = newDf.pop('Seniority')

    baseIndex = newDf.columns.get_loc('Base_Role')

    newDf.insert(baseIndex + 1, 'Seniority', seniorityCol)

    # print(newDf)

    newDf.to_csv("leveled.csv")

    return newDf
