"""
add a new hard coded column with value = "TEST" to tran_hdr dataframe

"""
"""
read transaction_hdr(1_jan_2019) data and convert it into pandas dataframe, similarly read transaction_dtl_data (1_jan_2019)

"""

import pandas as pd


print("####################################")
print("\n")

print("tran_hdr file : ")
path=r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_hdr_1_2019.csv"
# read tran_hdr_2019 file
df=pd.read_csv(path)
df.insert(4,"new_column",value="TEST")


print(df)
