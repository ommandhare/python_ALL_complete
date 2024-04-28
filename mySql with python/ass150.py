"""
Write a program to read product data from SQL in python program save it in dict
(save category as key and list of objects related to that category as value).
Take user input for category and display all product options in that category.

"""

import mysql.connector
import pandas

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='0777',
    database='retail'
)

cursor=conn.cursor()

query=("""
select category,description from product;
""")
cursor.execute(query)
result=cursor.fetchall()
# print(result)

sql_query = "SELECT description, category FROM product;"

# Execute SQL query
cursor.execute(sql_query)

# Fetch all rows
products_data = cursor.fetchall()

# Close MySQL connection
conn.close()

# Create dictionary to store product data by category
products_by_category = {}
for row in products_data:
    description, category = row
    product = description
    if category in products_by_category:
        products_by_category[category].append(product)
    else:
        products_by_category[category] = [product]

print(products_by_category)

findprod=input("Enter the category  :  ")

for k,v in products_by_category.items():
    if findprod in products_by_category:
        print("found")
        print("Items in ",k, "category :")
        print(v)
        break;

