"""
Write a program to read data from product table on mysql and find number of products by category
and insert this data in SQL table category_num_products
"""

import pandas as pd
import mysql.connector
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
query1 = (""" select category,count(product_id) from product 
               group by category;""")
cursor.execute(query1)
results = cursor.fetchall()
count = 0
print(results)

for line in results:
      print(tuple(line))
      query = f"INSERT INTO {'category_num_products'} VALUES {tuple(line)}"
     # for itr in range(len(data))
      cursor.execute(query)

conn.commit()

conn.close()

