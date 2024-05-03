import pandas as pd


tran_dtl=pd.read_csv(r"C:\Users\om\PycharmProjects\python_All\data\tran_dtl.csv")
print(tran_dtl)

product=pd.read_csv(r"C:\Users\om\PycharmProjects\python_All\data\product.csv")
print(product)


join=pd.merge(tran_dtl,product,left_on='product_id',right_on='ID')
print(join)

left_join=pd.merge(tran_dtl,product,left_on='product_id',right_on='ID',how='left')
print(left_join)

right_join=pd.merge(tran_dtl,product,left_on='product_id',right_on='ID',how='right')
print(right_join)