import csv

import pandas as pd

gPath = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Radar_Codes\global_synoym.csv"
bPath = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Radar_Codes\Baseword.csv"

synonyDict = {}

# =========================
# READ GLOBAL SYNONYM FILE
# =========================
with open(gPath, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    # ✅ Fix column names
    reader.fieldnames = [col.strip().lower() for col in reader.fieldnames]

    for dataTuple in reader:
        word = dataTuple.get("word")
        synonym = dataTuple.get("synonym")

        if word and synonym:
            synonyDict[word.strip()] = synonym.strip()

# =========================
# READ BASEWORD FILE
# =========================
with open(bPath, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    # ✅ Fix column names
    reader.fieldnames = [col.strip().lower() for col in reader.fieldnames]

    for dataTuple in reader:
        word = dataTuple.get("word")
        synonym = dataTuple.get("synonym")

        if word and synonym:
            if word.strip() not in synonyDict:
                synonyDict[word.strip()] = synonym.strip()

# =========================
# CREATE LIST (OUTSIDE LOOP ✅)
# =========================
allData = []

for word, synonym in synonyDict.items():
    allData.append([word, synonym])

finaldf=pd.DataFrame(allData)

finaldf.to_csv("Merged_Synoyms.csv")