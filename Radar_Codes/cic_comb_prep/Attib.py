import sys
import os
import pandas as pd
wpath=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Radar_Codes\word_attrib 1.csv"
path=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Radar_Codes\Synonym_Replaces.csv"
stop_word=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Radar_Codes\stop_words (1).csv"
# -------------------------- prep synonym word replace prg ----------------------------- #

prepDscData = []
impWordsDict = set()
nonVegWordsDict = set()
liqWordsDict = set()
stopWords = set()
# ------------------- extract data ----------------- #
for datatuple in open(path):
    sr, cic, newDsc, oldDsc, dept = datatuple.strip().split(",")
    prepDscData.append([cic, newDsc, oldDsc, dept])
for dataTuple in open(wpath):
    word,imp_flag=dataTuple.strip().split(",")# important word load
    # print(word)
    impWordsDict.add(word)
# for dataTuple in nonVegWordTable:  # non-veg word load
#     word = dataTuple["word"]
#     nonVegWordsDict.add(word)
# for dataTuple in liquidWordTable:  # liq word load
#     word = dataTuple["word"]
#     liqWordsDict.add(word)
for dataTuple in open(stop_word):  # stop word file
    st_words=dataTuple.strip()
    stopWords.add(word)
    # print(st_words)
# # ------------------ prepItem attrib program ------------- #
# # ------------------- get word freq -------------------- #
wordCnt = {}
for dataTuple in prepDscData:
    newDsc = dataTuple[1]
    for wd in newDsc.split():
          # print(wd)
        if len(wd) > 2:
            if wd not in wordCnt:
                wordCnt[wd] = 1
            else:
                wordCnt[wd] += 1
print('word count completed.')
# #   ---------------------- adding flags ------------------- #
allData = []
for dataTuple in prepDscData:
    cic, newDsc, oldDsc, dept = dataTuple
    tmpDsc = []
    dupWdDict = set()  # updated
    nonVegFlag = 0
    liqFlag = 0
    impWdCnt = 0
    effWdCnt = 0
    for word in newDsc.split():
        if word in stopWords:
            continue
        if word not in dupWdDict:  # updated
            tmpDsc.append(word)
        #     dupWdDict.add(word)  # updated
        # if word in nonVegWordsDict:
        #     nonVegFlag = 1
        # if word in liqWordsDict:
        #     liqFlag = 1
        if word in impWordsDict:
            # print(word)
            impWdCnt += 1
        if word in wordCnt and wordCnt[word] > 1 and len(word) > 2:
            effWdCnt += 1
    allData.append([cic, " ".join(tmpDsc), oldDsc, dept, impWdCnt, effWdCnt])
print('flaging dsc completed.')
print(allData)
# ---------------------- load data ---------------------------- #
df = pd.DataFrame(allData, columns=["cic", "new_cic_dsc", "old_cic_dsc", "dept", "imp_flag","effective_wrd_cnt"])
df.to_csv("Item_Attribut_table.csv")