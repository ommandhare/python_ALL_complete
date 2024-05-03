"""
find profile of numerical varialbe (min, max, quantile, mean, median, standard deviation) using pandas

"""

import pandas as pd

path=r"C:\Users\HP\Desktop\Philomath\SQL\Retail_Data\tran_dtl_1_2019.csv"
df=pd.read_csv(path)

print("###############################")
df_desc=df.describe()
print(df_desc)