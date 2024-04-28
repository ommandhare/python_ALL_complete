"""
read same file ,from create pandas dataframe and
replace missing values with separate values for each column.

"""

import pandas
import pandas as pd

print("\n")
df=pd.read_csv(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\pandas\tran_dtl_sample.csv",na_values = [""])
print(df)

values = {'tran_id':1000, 'product_id':1223.0,'qty':120020,'tran_dt':'2026-03-20'}
df5 = df.fillna(value=values)
print(df5)