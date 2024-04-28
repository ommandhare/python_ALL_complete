import pandas as pd
import numpy as np

df_member=pd.read_csv(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\member.csv")
print(df_member)
df_product=pd.read_csv(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\product.csv")
print(df_product)
df_tran_dtl=pd.read_csv(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_dtl_1_2019.csv")
print(df_tran_dtl)
df_tran_hdr=pd.read_csv(r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_hdr_1_2019.csv")
print(df_tran_hdr)


# New rows data
new_rows_data = {
    'product_id': [6, 7],
    'description': ['Muffins', 'Bagels'],
    'price': [np.nan,2.25],
    'category': ['Baked goods', np.nan],
    'max_qty': [5, 5]
}
print(new_rows_data)

df_4=pd.DataFrame(new_rows_data)
# print(df_product_new)

df_product=df_product._append(df_4,ignore_index=True)
print(df_product)

isna=df_product.isna().sum()
print(isna)

df_product['price'].fillna(df_product['price'].mean(),inplace=True)
# df_product.dropna(inplace=True)
df_product['category'].fillna(df_product['category'].mode()[0],inplace=True)
# df_product['category']=df_product.fillna(Snacks)
print(df_product)

df_date=df['tran_dt']
print(df_date)
