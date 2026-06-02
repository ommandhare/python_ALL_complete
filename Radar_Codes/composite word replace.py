cpath=r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\Radar_Codes\composite word.csv"
import pandas as pd
import mysql.connector
import re
from utility import combUtility as c
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


compWordDict = {}
for dataTuple in open(cpath):
    cmbStr,comb_freq,comb_size,comb_detail_str,conf_detail_str,composite_flag=dataTuple.split(",")
    cmbStr=cmbStr.upper()
    cmbLst = cmbStr.split('#')
    for wd in cmbLst:
        wd=wd.upper()
        compWordDict[wd] = (cmbStr,len(cmbLst))

print(compWordDict)

allData=[]
for datatuple in data:
    dept_id, dept_nm, group_id, group_dsc, category_id, category_dsc, sub_category_id, sub_category_dsc, upc_nbr, product_id, product_dsc, insert_date = datatuple
    product_dsc=product_dsc.upper()
    dscLst = re.findall(r'[A-Z]+', product_dsc)
    print(dscLst)
    filterWords = " ".join(set(dscLst))
    sortedWords = " ".join(sorted(filterWords.split()))
    print(sortedWords)
    # print(compWordDict)
    tmpDesc = str(c.compReplace(compWordDict, sortedWords))
    print(f"Changed Word ----{tmpDesc}")
    allData.append([product_id, tmpDesc, product_dsc, dept_nm])
    # print(product_dsc)
    # print("-------")
    # print(tmpDesc)
    df = pd.DataFrame(allData, columns=["product_id", "new_product_dsc", "product_dsc", "dept_nm"])


df.to_csv("composite comb replaced.csv", index=False, mode='a')
print("Done")

print(df)