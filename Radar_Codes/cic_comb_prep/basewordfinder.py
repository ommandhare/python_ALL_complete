import pandas as pd
import mysql.connector
import re
from utility import simUtility as su
# =========================
# MYSQL CONNECTION
# =========================

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0777",
    database="mockproject"
)

cursor = conn.cursor()


# =========================
# CREATE TABLE
# =========================

# Query = """
#
# SELECT * FROM item_master_v2_final
#
# """

# cursor.execute(Query)

# data=cursor.fetchall()
def loadSet(output,input):
    for wd in input:
        output.add(wd)
def genSynonymsData(word,wordLenDict,wordCntDict):
    baseWd = word
    wordSize = len(word)
    allDataSet = set()
    for i in range(wordSize-2,wordSize+3):
        if i in wordLenDict and word[0] in wordLenDict[i]:
            loadSet(allDataSet,wordLenDict[i][word[0]])

    simList = []
    for target in allDataSet:
        if su.nGrams(baseWd,target) > 0.60: #or levenstine(baseWd,target) > 0.75:
            if wordCntDict[target] > wordCntDict[baseWd]:
                baseWd = target
            simList.append(target)
    return baseWd,simList






path= r"/Radar_Codes/Word Count.csv"

wordCntDict = {}
wordLenDict = {}
wordLst = []
allData = []
for datatuple in open(path):
    sr_no,word,freq=datatuple.strip().split(",")
    if len(word) < 3:
        continue
    wordCntDict[word] = freq
    wordLst.append(word)
    if len(word) not in wordLenDict:  # if size is not in dict
        wordLenDict[len(word)] = {word[0]: {word}}
    else:
        if word[0] not in wordLenDict[len(word)]:  # if size is there but first character set is not
            wordLenDict[len(word)][word[0]] = {word}
        else:
            wordLenDict[len(word)][word[0]].add(word)  # just add word in right place
    # print("data Loaded")
    # print(wordLenDict)
    wordLst.sort(key= lambda x:wordCntDict[x],reverse=True) # sort words by freq dsc
    wordBaseWordDict = {}
    for word in wordLst:
        if word in wordBaseWordDict:
            continue
        baseWd, simList = genSynonymsData(word, wordLenDict, wordCntDict)
        for wd in simList:
            wordBaseWordDict[wd] = baseWd
            wordLenDict[len(wd)][wd[0]].remove(wd)
    # print("synonym finder done")
    # print(wordLst)

    for word, baseword in wordBaseWordDict.items():
        allData.append([word, baseword])
    # --------------------------- load data to table ------------------------ #

df=pd.DataFrame(allData,columns=["word", "synonym"])

df.to_csv("Baseword.csv")