import pandas as pd
import csv

path=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Radar_Codes\Item_Attribut_table.csv"
wordDict={}
with open(path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for dataTuple in reader:
        newDsc=dataTuple["new_cic_dsc"]
        wordLst = newDsc.split()
        for word in wordLst:
            if word in wordDict:
                cnt = wordDict[word]
                wordDict[word] = cnt + 1
            else:
                wordDict[word] = 1

allData = []
for word, cnt in wordDict.items():
    allData.append([word, cnt])
# ------------load data into table--------------------- #
df = pd.DataFrame(allData, columns=["word", "freq"])

df.to_csv("Word_Count.csv")
