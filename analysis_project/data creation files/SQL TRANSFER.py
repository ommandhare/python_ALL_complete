import pandas as pd
from sqlalchemy import create_engine





path= r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\analysis_project\daily_files\member.csv" #path of csv file

data=pd.read_csv(path)

print(data)

engine = create_engine('mysql+pymysql://root:0777@localhost:3306/retail_project')  #username pass database name

data.to_sql('member', con=engine, if_exists='replace', index=False)
# table name
print("done")