import pandas as pd
import mysql.connector
import re
from utility import combUtility as cu
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
Finaldata=[]
for r in range(2,6):
    wordDict={}
    pattern = re.compile(r'[A-Z]+')
    wordCnt = {}
    dscCombDict={}
    for datatuple in data:
        dept_id, dept_nm, group_id, group_dsc, category_id, category_dsc, sub_category_id, sub_category_dsc, upc_nbr, product_id, product_dsc, insert_date = datatuple

        words = product_dsc.split(" ")
        words=sorted(words)
        # for word in words:
        #     print(word)
        for word in words:
            if word not in wordCnt:
                wordCnt[word] = 1    #word freq
            else:
                wordCnt[word] += 1
        wordCombs = []
        cu.ncr(words, 0, len(words), wordCombs, r, [])   #generating combinations
        if len(wordCombs) == 0:  # skip dsc if r size combi cannot be created.
            continue
        # print(wordCombs)    #Combination of 2 r=2
        for cmbLst in wordCombs:
            cmbStr = "#".join(cmbLst)
            if cmbStr not in dscCombDict:    # frequency of combination
                dscCombDict[cmbStr] = 1
            else:
                dscCombDict[cmbStr] += 1
    # print(dscCombDict)
        allData = []
        for cmbStr, cmbFreq in dscCombDict.items():
            if cmbFreq < 2:
                continue
            # ------- gen confidence of combination -------------------- #
            confLst = []
            confFlag = 1
            for word in cmbStr.split('#'):
                # print(f"{word},---{cmbStr}")
                currConf = cmbFreq / wordCnt[word]
                # print(f"CmbFreq...{cmbFreq}---wordcount of word {wordCnt[word]}-----confindence..{currConf}")
                if currConf < 0.75 or wordCnt[word] <= 1:
                    confFlag = 0
                confLst.append(f'{word}~{round(currConf, 2)}')
            confStr = "#:#".join(confLst)         #DEL~1.0#:#MONTE~1.0
            # print(confStr)
            if confFlag == 0:
                continue
            # -------- gen wordFreqStr ---------------- #
            wordFreqLst = []
            for wd in cmbStr.split('#'):
                wordFreqLst.append(f'{wd}~{wordCnt[wd]}')
            wordFreqStr = "#:#".join(wordFreqLst)
            allData.append([cmbStr, cmbFreq, r, wordFreqStr, confStr, confFlag])
            # print("Hi")
    df = pd.DataFrame(
        allData,
        columns=[
            "comb_str",
            "comb_freq",
            "comb_size",
            "comb_detail_str",
            "conf_detail_str",
            "composite_flag"
        ]
    )
    print(df)
    df.to_csv("composite word.csv", index=False,mode='a',header=False)
    print(f"{r}__completed")
print("✅ CSV created successfully")

# print(Finaldata)