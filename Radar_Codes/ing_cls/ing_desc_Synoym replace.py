import csv
import mysql.connector
import re
import pandas as pd

merged_Synoyms=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Radar_Codes\cic_comb_prep\Merged_Synoyms.csv"
stop_words=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Radar_Codes\cic_comb_prep\stop_words (1).csv"

def baseWordReplacing(baseWordDict, snt):
    sntLst = snt.split()
    for idx in range(len(sntLst)):
        if sntLst[idx] in baseWordDict:
            sntLst[idx] = baseWordDict[sntLst[idx]]
    return " ".join(sntLst)


def cleanDes(stn, wordCnt, stopWords):
    stnLst = stn.split()
    cleanStnLst = set()
    for idx in range(len(stnLst)):
        word = stnLst[idx]
        if word in stopWords:
            continue
        if word in wordCnt:
            if wordCnt[word] > 1 and len(word) > 1:
                cleanStnLst.add(word)
        elif len(word) > 2:
            cleanStnLst.add(word)
    return " ".join(cleanStnLst)





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

Query = """

SELECT * FROM item_master_v2_final

"""

cursor.execute(Query)

data=cursor.fetchall()
# print(data)
wordDict={}
pattern = re.compile(r'[A-Z]+')
stop_word=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Radar_Codes\stop_words (1).csv"
stopWords = set()
for dataTuple in open(stop_words):  # stop word file
    st_words=dataTuple.strip()
    stopWords.add(st_words)


wordBaseWord = {}
with open(merged_Synoyms, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for dataTuple in reader:
     word = dataTuple["word"]
     synonym = dataTuple["synonym"]
     wordBaseWord[word] = synonym

wordCntDict ={}
ingData = []
for datatuple in data:
    dept_id, dept_nm, group_id, group_dsc, category_id, category_dsc, sub_category_id, sub_category_dsc, upc_nbr, product_id, product_dsc, insert_date = datatuple
    # print(product_dsc,"OLDDDDD")
    product_dsc=product_dsc.upper()
    ingDscLst = re.findall(r'[A-Z]+', product_dsc)
    ingDscWdOnly = " ".join(ingDscLst).upper()
    repDesc = baseWordReplacing(wordBaseWord, ingDscWdOnly)
    ingData.append([product_id, product_dsc.replace(',', ' '), repDesc])
    for word in repDesc.split():
        if word not in wordCntDict:
            wordCntDict[word] = 1
        else:
            wordCntDict[word] += 1

ingDataNew = []
for ingDataTuple in ingData:
    ingId, oldDsc, currDsc = ingDataTuple
    clnDesc = cleanDes(currDsc, wordCntDict, stopWords)
    newDesc = " ".join(sorted(clnDesc.split()))
    # print(newDesc)
    ingDataNew.append([ingId, oldDsc.replace(",", " "), newDesc, ])
    for word in repDesc.split():
        if word not in wordCntDict:
            wordCntDict[word] = 1
        else:
            wordCntDict[word]+=1
ingDataNew = []
for ingDataTuple in ingData:
    ingId, oldDsc, currDsc = ingDataTuple
    # print(currDsc)
    clnDesc = cleanDes(currDsc, wordCntDict, stopWords)
    newDesc = " ".join(sorted(clnDesc.split()))
    ingDataNew.append([ingId, oldDsc.replace(",", " "), newDesc])
    # print(newDesc)
    # print(ingDataNew)


print(ingDataNew)
df=pd.DataFrame(ingDataNew)
df.to_csv("Ing_desc_replaced.csv")