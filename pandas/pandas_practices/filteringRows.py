import pandas as pd

df=pd.read_csv(r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\pandas\pandas_practices\product.csv")

# Selecting particular rows
# print(df[5:11])

# Selecting rows Filter wise
# print(df[df.category=="Beverages"])

# booleans operators
# print(df[df.price>3])
