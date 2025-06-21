import pandas as pd

# Displaying all columns and rows
# pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',None)

df=pd.read_csv(r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\pandas\pandas_practices\product.csv")

# print DataFrame
print(df)
#
# # print columns
# print(df.columns)
#
# # print head and tail
# print(df.head())
# print(df.tail())

# shape
# print(df.shape)
#
# #Stats About Each Columns
print(df.describe())


# print("Sum")
# print(df.qty.sum())

# print("mean")
# print(df.qty.mean())

# print("median")
# print(df.qty.median())

