import pandas as pd


df1=pd.read_csv(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_dtl_1_2019.csv")
# print(df1)

df2=pd.read_csv(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_hdr_1_2019.csv")
# print(df2)

df1=df1.rename(columns={'tran_id': 't_id', 'tran_dt': 't_dt'})
df2=df2.rename(columns={'tran_id': 't_id', 'tran_dt': 't_dt'})

df_merge1=pd.merge(df1,df2,left_on='t_id',right_on='t_id')
print(df_merge1)
