"""
add some missing values in raw data in tran_dtl file (create a separate file)..
Read this file, create a pandas dataframe and replace missing value with 1.
default value, forward fill, backward fill.

"""


import pandas
import pandas as pd
print("fill 0 ::")
print("\n")
df=pd.read_csv(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\pandas\tran_dtl_sample.csv",na_values = [""])
df_fill_1 = df.fillna(1)
print(df_fill_1)

print("ffill::")
print("\n")
df=pd.read_csv(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\pandas\tran_dtl_sample.csv",na_values = [""])
df_ffill = df.ffill()
print(df_ffill)

print("bfill::")
print("\n")
df=pd.read_csv(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\pandas\tran_dtl_sample.csv",na_values = [""])
df_bfill = df.bfill()
print(df_bfill)