"""
Write a program to read data from transaction table on mysql as pandas data frame,
find aggregate monthly sale (in pandas) and write it to csv and SQL Table (monthly_sale)

"""


import pandas as pd
import mysql.connector
import schedule
import csv
import time

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0777',
    database='retail'
)

cursor = conn.cursor()

# product_csv generator
query1 = (""" select * from tran_dtl;""")
cursor.execute(query1)
results = cursor.fetchall()
count = 0
# print(results)

df=pd.read_sql(query1,conn)
print(df)

grouped = df.groupby('tran_dt')

avg_sale=grouped['amt'].mean()

print(avg_sale)
avg_path = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\mySql with python\avg_monthly_sale.csv"

avg_sale.to_csv(avg_path)
