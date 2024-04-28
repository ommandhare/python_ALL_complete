"""
Write a program to read data from Product table on mysql and write it to a csv file
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
    database='retail_project'
)

cursor = conn.cursor()

# product_csv generator
query1 = (""" select category,count(product_id) from product 
               group by category;""")
cursor.execute(query1)
results1 = cursor.fetchall()
count = 0
print(results1)
prod_path = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\subprocess\products_by_category.csv"
with open(prod_path, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, results1)
    csv_writer.writerow(['Category', 'count_of_products'])
    csv_writer.writerows(results1)

print(f"Data has been written to {prod_path}")