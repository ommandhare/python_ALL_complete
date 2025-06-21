import pandas as pd
import string as str
df=pd.read_csv(r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\pandas\pandas_practices\product.csv")

# Arithmetic Operation on Columns
# print(df['price']+df['qty'])

# Adding or Concatenating String
# print(df['Name']+"_"+df['category'])

#just Selecting Columns
# print(df[['Name','category']])


# replacing string
# print(df['category'].str.replace('Snacks','drinks'))
