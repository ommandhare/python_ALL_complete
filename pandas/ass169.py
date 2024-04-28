"""
calculate total sales by year, month and product description
(use dataframe prepared in previous assignment)

"""

import mysql.connector
import pandas
import pandas as pd
import datetime as dt
from datetime import timedelta

pd.set_option("display.max_columns",None)

pd.set_option("display.min_rows",500)
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



salesby=joined_df.groupby('tran_dt')['amt'].count()

print(salesby)
joined_df['tran_dt']=pd.to_datetime(joined_df['tran_dt'])

joined_df['year']=joined_df['tran_dt'].dt.year

joined_df['month']=joined_df['tran_dt'].dt.month

# print("JOINED")
# print(joined_df)

sales_by_year_month_product = joined_df.groupby(['year','month','description'])['amt'].sum()

print(sales_by_year_month_product)

