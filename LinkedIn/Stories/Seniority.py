import csv
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

path=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Stories\Updated Connection.csv"
cnt=0

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

def extract_levels(position):

    # position = clean_position(position)

    foundLevels = []

    # First check full phrase matches
    for keyword in levelDict:

        if keyword.lower() in position.lower():

            foundLevels.append(levelDict[keyword])

    return list(set(foundLevels))


df=pd.read_csv(path)
# with open(path, newline='', encoding='utf-8') as file:
#     reader = csv.reader(file)
#     levellist=[]
#     for line in reader:
#         if cnt == 0:
#             cnt += 1
#             continue
#
#         First_Name,Last_Name,URL,Email_Address,Company,Position, base_role ,Connected_On = line
#         print(Position)
#         levellist=extract_levels(Position)
#         print(levellist)

seniorityList = []

newRows = []

for _, row in df.iterrows():

    position = str(row['Position'])

    levels = extract_levels(position)

    if len(levels) == 0:
        levels = ["Unknown"]

    for level in levels:

        newRow = row.copy()

        newRow['Seniority'] = level

        newRows.append(newRow)


newDf = pd.DataFrame(newRows)

print(newDf)

newDf.to_csv("output.csv")