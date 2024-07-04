import pandas as pd
from sqlalchemy import create_engine





path= r"C:\Users\om\PycharmProjects\python_All\analysis_project\daily_files\product.csv"  #path of csv file

data=pd.read_csv(path)

print(data)

engine = create_engine('mysql+pymysql://root:0777@localhost:3306/sample')  #username pass database name

data.to_sql('product', con=engine, if_exists='replace', index=False)
# table name
print("done")