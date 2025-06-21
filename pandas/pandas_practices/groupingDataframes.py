import pandas as pd


df1 = pd.read_csv("product.csv")
# print(df1)


# print(df1.groupby('category').aggregate('qty').sum())

# Alternate way
# print(df1.groupby('category').aggregate({'qty':'sum'}))

print(df1.groupby('category').aggregate({'qty':['sum','median']}))