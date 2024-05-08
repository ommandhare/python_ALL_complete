import pandas as pd

path = r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\product.csv"

df = pd.read_csv(path)

df1 = df[df['category']=='Grocery']
# print(df1)

df2 = df[df['category']!='Beverages']
print(df2)


df_tran_dtl=pd.read_csv(r"C:\Users\HP\Desktop\Philomath\SQL\mySql\Retail_Data\tran_dtl_1_2019.csv")
# header=None,names=["tran_id","product_id","qty","amt","tran_dtl"]
column=['tran_id','product_id','qty','amt','tran_dt']
df_tran_dtl.columns=column
print(df_tran_dtl)

df_tran_hdr=pd.read_csv(r"C:\Users\HP\Desktop\Philomath\SQL\mySql\Retail_Data\tran_hdr_1_2019.csv",header=None,names=["tran_id","store_id","member_id","tran_dtl"])
print(df_tran_hdr)

print("GROUP BY ###############")

print("total transaction per product>>>>>>>\n")
total_tran = df_tran_dtl.groupby('product_id')['tran_id'].count()
print(total_tran)
print("total qty per product >>>>>>>>>\n")
total_qty = df_tran_dtl.groupby('product_id')['qty'].sum()
print(total_qty)

df_member=pd.read_csv(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\member.csv")

df_product=pd.read_csv(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\product.csv")
df_tran_dtl=pd.read_csv(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_dtl_1_2019.csv")
df_tran_hdr=pd.read_csv(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_hdr_1_2019.csv")