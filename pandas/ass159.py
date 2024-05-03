"""
filter tran_dtl_dataframe  on qty > 4

"""

import pandas as pd

path=r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_dtl_1_2019.csv"
df=pd.read_csv(path)

df_filter=[df.qty>4]

print(df_filter)