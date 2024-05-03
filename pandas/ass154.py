"""
read transaction_hdr file and convert it into pandas dataframe.
Print top 10 and bottom 10 records (head and tail) to see sample data.

"""

import pandas as pd

path=r"C:\Users\om\PycharmProjects\python_All\data\tran_dtl.csv"
# read csv file
df1=pd.read_csv(path)


df1_head=df1.head(10)
print(df1_head)

print("#########################################")

print("\n")
df1_tail=df1.tail(10)
print(df1_tail)



