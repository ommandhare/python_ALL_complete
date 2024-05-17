"""
find profile of numerical variable (min, max, quantile, mean, median, standard deviation) using pandas

"""

import pandas as pd

path=r"C:\Users\om\PycharmProjects\python_All\data\product.csv"
df=pd.read_csv(path)

print("###############################")
df_desc=df.describe()
print(df_desc)