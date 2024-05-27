import pandas as pd
from sqlalchemy import create_engine

path= r"/data/itm_enc_dsc_data.csv"

data=pd.read_csv(path)

print(data)

engine = create_engine('mysql+pymysql://root:0777@localhost:3306/radar')

data.to_sql('item_desc', con=engine, if_exists='replace', index=False)

print("done")
