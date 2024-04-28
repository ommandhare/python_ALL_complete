"""
read product data and tran_dtl data from mySQL to pandas dataframe. Join two data frames

"""

import mysql.connector
import pandas
import pandas as pd
import datetime as dt
from datetime import timedelta

conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='0777',
    database='retail'
)

cursor=conn.cursor()

query1=("""
select * from tran_dtl;
""")

query2=("""
select * from product;
""")

tran_dtl_df=pd.read_sql(query1,conn)
product_df=pd.read_sql(query2,conn)

joined_df=pd.merge(tran_dtl_df,product_df,on='product_id',how='left')

print(joined_df)