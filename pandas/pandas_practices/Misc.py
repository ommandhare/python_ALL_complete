import pandas as pd

df1 = pd.read_csv("product.csv")

# descending
# print(df1.sort_values('price',ascending=False))

# aescending
# print(df1.sort_values('price',ascending=False))



# DROPPING COLUMNS
# print(df1.drop(columns=['ID','price']))

# Getting Samples
print(df1.sample(5))