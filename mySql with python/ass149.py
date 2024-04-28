"""
Write a program to read product data from SQL in python program save it in dict
(save id as key and object as value).
Take user input for product description and find if product exists and if it exists then display produt details.

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
select product_id,description from product;
""")
cursor.execute(query)
result=cursor.fetchall()
print(result)

product={}

for row in result:
    product_id,description=row
    product[product_id]=description

print(product)

search_description=input("enter product desc  : ")
print(search_description)

# for product_id, product_info in product.items():
#  print(product_info)
for product_id, product_info in product.items():
        if search_description == product_info:
          print("found")
          print(product_id, ":" ,product_info)
        else:
         print("not found")
         break