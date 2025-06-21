import altair as alt
import pandas as pd
# Displaying all columns and rows
pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)


product = pd.read_csv("product.csv")

tran_dtl = pd.read_csv("tran_dtl.csv")

# INNER JOIN
# inner_join = product.merge(tran_dtl, left_on='ID', right_on='product_id', how='inner')
#
# print(inner_join.sample(5))



# LEFT JOIN
# left_join = pd.merge(product,tran_dtl, left_on='ID', right_on='product_id', how='left')
# #
# print(left_join.sample(5))



# Graph
chart = alt.Chart(product).mark_point().encode(
    x='category',
    y='price',
    size='qty',
    color='Name'  # or any other categorical/quantitative field
)

chart.show()
chart.save(r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\pandas\pandas_practices\graph.html")