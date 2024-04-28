"""
Write a program to read total sale by member by product for last 12 months (use SQL to get agg data)
in pandas dataframe, find max sale product for every member,
min sale product for every member and write it to two separate fils
(1. sale by member, by product. 2. min and max sale and product by member)

"""


import pandas as pd
import mysql.connector


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0777',
    database='retail'
)


cursor = conn.cursor()
query1=("""

select member_id,product_id,sum(amt) as total_sale from tran_dtl td
join tran_hdr th on td.tran_id=th.tran_id
WHERE td.tran_dt < current_date() AND td.tran_dt >= DATE_SUB(CURRENT_DATE(), interval 1 year)
group by member_id,product_id;
""")

cursor.execute(query1)
results=cursor.fetchall()
print(results)

df=pd.read_sql(query1,conn)
print(df)


print("####  MAX SALE PER member")

df_max_sale=df.groupby('member_id')['total_sale'].max()

print(df_max_sale)

df_max_sale.to_csv(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\mySql with python\max_salemem.csv")

print("####  MIN SALE PER member")

df_min_sale=df.groupby('member_id')['total_sale'].min()

print(df_min_sale)

df_max_sale.to_csv(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\mySql with python\min_salemem.csv")
