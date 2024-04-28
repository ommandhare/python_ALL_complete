"""
join tran_hdr and tran_detail dataframes using join conditions on two columns tran_id and tran_dt

"""


import pandas as pd


df1=pd.read_csv(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_dtl_1_2019.csv")
# print(df1)

df2=pd.read_csv(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_hdr_1_2019.csv")
# print(df2)

df_merge1=pd.merge(df1,df2,left_on='tran_dt',right_on='tran_id')
print(df_merge1)

df_merge2=pd.merge(df1,df2,on=['tran_dt','tran_dt'])
print(df_merge2)