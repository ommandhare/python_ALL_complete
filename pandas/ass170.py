"""
calculate rolling 3 months sale (current and two previous) by product, year and month

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



joined_df['tran_dt']=pd.to_datetime(joined_df['tran_dt'])

joined_df['year']=joined_df['tran_dt'].dt.year

joined_df['month']=joined_df['tran_dt'].dt.month

# print("JOINED")
# print(joined_df)


rolling_sales = joined_df.groupby(['product_id', 'year','month'])['amt'].sum().reset_index()
# rolling_sales['rolling_2_months_sale'] = rolling_sales.groupby('product_id')['amt'].rolling(window=2, min_periods=1).sum().values
rolling_sales['rolling_3_months_sale'] = rolling_sales.groupby(['product_id'])['amt'].rolling(window=3, min_periods=1).sum().values

print(rolling_sales)
