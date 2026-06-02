import pandas as pd
import mysql.connector
import re
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

for datatuple in data:
    dept_id, dept_nm, group_id, group_dsc, category_id, category_dsc, sub_category_id, sub_category_dsc, upc_nbr, product_id, product_dsc, insert_date = datatuple

    words = product_dsc.split(" ")
    for word in words:
        if pattern.match(word):
            if word not in wordDict:
                word=word.upper()
                wordDict[word] = 1
            else:
                word=word.upper()
                wordDict[word] += 1
    allData = []
    for word, freq in wordDict.items():
        allData.append([word, freq])

# print(allData)

df = (pd.DataFrame(allData, columns=["word", "freq"]))


df.to_csv("Word Count.csv")
