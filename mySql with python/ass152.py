"""
Write a program to get todays date or user input date,
read rolling 12 month data from SQL (tran_dtl table and tran_hdr table) in pandas dataframe,
read product table in pandas data frame. Calculate score for every category for every member.

"""


import mysql.connector
import pandas
import pandas as pd
import datetime as dt
from datetime import timedelta

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='0777',
    database='retail'
)

cursor=conn.cursor()

query1=("""
select * from tran_dtl;
""")
cursor.execute(query1)
tran_dtl=cursor.fetchall()
query2=("""
select * from tran_hdr;
""")
cursor.execute(query2)
tran_hdr=cursor.fetchall()


query3=("""
select * from product;
""")
cursor.execute(query3)
product=cursor.fetchall()


tran_dtl_df=pd.read_sql(query1,conn)
# print(tran_dtl_df)

tran_hdr_df=pd.read_sql(query2,conn)
# print(tran_hdr_df)

product_df=pd.read_sql(query3,conn)
# print(tran_hdr_df)

date=dt.date(2022,3,20)

print(date)

roll_data=date-timedelta(days=365)
print(roll_data)


merge1=pd.merge(tran_dtl_df,tran_hdr_df,on='tran_id',how="right")
total_merge=pd.merge(merge1,product_df,on='product_id',how="left")

print(total_merge)

total_merge.to_csv(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\mySql with python\total.csv")


every_category_for_member=total_merge.groupby('member_id')['category'].count()
print(every_category_for_member)
