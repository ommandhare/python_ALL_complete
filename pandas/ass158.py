"""
add new column to tran_dtl dataframe ==> new column is "price" = sales_amt/qty

"""

import pandas as pd
print("###############################")
path=r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_dtl_1_2019.csv"
df=pd.read_csv(path)

df["price"]=df.amt/df.qty

print(df)

