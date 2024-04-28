"""
join tran_hdr, and tran_detail dataframes using pandas (try inner, outer, left outer, right outer joins)

"""


import pandas as pd


df1=pd.read_csv(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_dtl_1_2019.csv")
# print(df1)

df2=pd.read_csv(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_hdr_1_2019.csv")
# print(df2)


df_merge=pd.merge(df1,df2,left_on='tran_id', right_on='tran_id')
print("inner join")
print(df_merge)


df_merge_left=pd.merge(df1,df2,left_on='tran_id', right_on='tran_id' ,how='left')
print("left join")
print(df_merge_left)


df_merge_right=pd.merge(df1,df2,left_on='tran_id', right_on='tran_id' ,how='right')
print("right join")
print(df_merge_right)


df_merge_outer=pd.merge(df1,df2,left_on='tran_id', right_on='tran_id' ,how='outer')
print("outer join")
print(df_merge_outer)
