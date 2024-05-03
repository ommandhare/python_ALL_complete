"""
read tran_detail file, create pandas data frame and do slicing and dicing (select only partial columns and rows)

"""
import pandas as pd
print("###############################")
path=r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_dtl_1_2019.csv"
df=pd.read_csv(path)

print("SLICE BY ROWS-------------------------------------------------------------")
df_rows = df[3:7]
print(df_rows)

print("SLICE BY COLUMNS")
df_col = df[["product_id","amt","tran_dt"]]
print(df_col)