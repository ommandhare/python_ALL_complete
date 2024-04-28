"""
Write a program to get todays date or user input date, read rolling 12 month data from SQL
(tran_dtl table and tran_hdr table) in pandas dataframe,
aggregate by member, by product and normalize data to get score for every produt for every member.

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

tran_dtl_df=pd.read_sql(query1,conn)
# print(tran_dtl_df)

tran_hdr_df=pd.read_sql(query2,conn)
# print(tran_hdr_df)

date=dt.date(2022,3,20)

print(date)

roll_data=date-timedelta(days=365)
print(roll_data)





print("\n")
print("BY Product id count of tran_id")
by_product =tran_dtl_df.groupby('product_id')['tran_id'].count()

print(by_product)

print("\n")
print("BY Member_id count of tran_id")
by_member =tran_hdr_df.groupby('member_id')['tran_id'].count()

print(by_member)


print("\n")
print("Merger")
Merge =pd.merge(tran_dtl_df,tran_hdr_df,on="tran_id",how="left")
print(Merge)


print("\n")
print("tran_id by_product_by_member  :")
by_product_by_member=Merge.groupby('member_id')['tran_id'].count()

print(by_product_by_member)





