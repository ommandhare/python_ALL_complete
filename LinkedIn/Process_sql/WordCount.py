import pandas as pd
import csv
import re
import unicodedata



def wordCount(df):
    # path=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\LinkedIn\Mandar_kale_connection.csv"
    posLst=[]
    comLst=[]
    wordLst=[]
    nameLst=[]
    roleWrdDict={}
    comDict={}
    cnt=0


    def clean_text(txt):
        txt = str(txt)

        # Remove corrupted UTF patterns
        txt = re.sub(r'â\S*', ' ', txt)

        # Normalize unicode
        txt = unicodedata.normalize('NFKD', txt)

        # Convert accented chars to ASCII
        txt = txt.encode('ascii', 'ignore').decode('utf-8')

        # Replace &
        txt = txt.replace("&", "and")

        # Keep only letters/numbers/spaces
        txt = re.sub(r'[^A-Za-z0-9 ]', '', txt)

        # Remove extra spaces
        txt = " ".join(txt.split())

        return txt



# df is the DataFrame passed to the function

    for _, row in df.iterrows():

        First_Name = row["First_Name"]
        Last_Name = row["Last_Name"]
        URL = row["URL"]
        Email_Address = row["Email_Address"]
        Company = row["Company"]
        Position = row["Position"]
        Connected_On = row["Connected_On"]

        posLst.append(Position)
        comLst.append(Company)
        nameLst.append(First_Name)



    # print(posLst)

    for role in posLst:
        clean_role = role.replace("(", "") \
            .replace(")", "") \
            .replace(",", "") \
            .replace("'", "") \
            .replace("/", " ")

        words = clean_role.split()
        for word in words:
            # print(word)
            wordLst.append(word)

    # print(cleanWordLst)

    for word in wordLst:
        if len(word)==1 or word=="and":
            continue
        else:
            if word not in roleWrdDict:
                roleWrdDict[word] = 1
            else:
                roleWrdDict[word] += 1

    # print(roleWrdDict)


    for company in comLst:

        company=clean_text(company)

        if company not in comDict:
            comDict[company] = 1
        else:
            comDict[company] += 1

    # print(comDict)

    # print(roleWrdDict)




    dfcom = pd.DataFrame(list(comDict.items()), columns=["Company", "Count"])


    dfrole = pd.DataFrame(list(roleWrdDict.items()), columns=["Role", "Count"])


    with pd.ExcelWriter("word and Company Count.xlsx") as writer:
        dfcom.to_excel(writer, sheet_name="Companies", index=False)
        dfrole.to_excel(writer, sheet_name="Roles", index=False)

    print("Excel and CSV files created")

    return dfrole, dfcom

