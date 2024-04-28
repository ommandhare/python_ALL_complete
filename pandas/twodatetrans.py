

import pandas as pd

df = pd.read_csv(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\tran_dtl.csv")

print(df)
df['tran_dt'] = pd.to_datetime(df['tran_dt'])

start_date = '2021-03-20'
end_date = '2021-04-20'

filter_df = df[(df['tran_dt'] >= start_date) & (df['tran_dt'] <= end_date)]


print(filter_df)
