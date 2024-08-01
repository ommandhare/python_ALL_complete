import pandas as pd
from sqlalchemy import create_engine





path= r"C:\Users\Om Mandhare\Documents\moving_avg_fact.csv" #path of csv file

data=pd.read_csv(path)

print(data)

engine = create_engine('mysql+pymysql://root:0777@localhost:3306/stock')  #username pass database name

data.to_sql('moving_avg_fact', con=engine, if_exists='replace', index=False)
# table name
print("done")