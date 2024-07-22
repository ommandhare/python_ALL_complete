import pandas as pd

path=r"C:\Users\om\PycharmProjects\python_All\analysis_project\daily_files\product.csv"

df=pd.read_csv(path)


df1 = df[df['category']=='Grocery']

print(df1)