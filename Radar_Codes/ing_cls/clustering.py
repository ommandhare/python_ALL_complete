import csv
import pandas as pd
from simUtility import wgtLevenstine,onlyWords
path=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Radar_Codes\ing_cls\Ing_desc_replaced.csv"
itemData=[]
with open(path, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for ingTuple in reader:
        ingId = ingTuple["0"]
        oldDsc = ingTuple["1"]
        newDsc = ingTuple["2"]
        itemTuple = (ingId, newDsc) if len(newDsc) > 2 else (ingId, " ".join(onlyWords(oldDsc.upper())))
        itemData.append(itemTuple)

    sortedList = sorted(itemData, key=lambda x: len(x[1]), reverse=True)

    # for item in sortedList:
    #    print("ID: ",item.id, " DES: ",item.name, " LEN: ",item.freq)
    print("clustring .../")
    itemDict = {}
    size = len(sortedList)
    for i in range(size - 1):
        # check if i is present in itemDict
        if (sortedList[i][0] in itemDict):
            continue
        for j in range(i + 1, size):
            if (wgtLevenstine(sortedList[i][1], sortedList[j][1]) > 0.75):
                # cluster formed
                # i is cluster center
                # j belongs to i
                if (sortedList[i][0] not in itemDict):
                    itemDict[sortedList[i][0]] = sortedList[i][0]
                if (sortedList[j][0] not in itemDict):
                    itemDict[sortedList[j][0]] = sortedList[i][0]

        if (sortedList[i][0] not in itemDict):
            itemDict[sortedList[i][0]] = sortedList[i][0]

df = pd.DataFrame(itemDict.items(), columns=["ing_id", "cls_rep_id"])
print(df)
df.to_csv("Clusters.csv")