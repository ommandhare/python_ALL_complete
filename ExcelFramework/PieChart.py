import pandas as pd
from openpyxl import Workbook
from openpyxl.chart import PieChart, Reference

# --------------------------
# 1. Pandas DataFrame
# --------------------------
# df = pd.DataFrame({
#     'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
#     'Sales': [40, 60, 80, 20]
# })
df_product=pd.read_csv(r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\ExcelFramework\product.csv")
df=df_product[['Name'],['price']]
print(df)
# --------------------------
# 2. Create Excel Workbook
# --------------------------
# wb = Workbook()
# ws = wb.active
# ws.title = "SalesData"
#
# # --------------------------
# # 3. Write Pandas DataFrame to Excel manually
# # (This avoids auto filters)
# # --------------------------
# # Write header
# ws.append(list(df.columns))
#
# # Write data rows
# for row in df.itertuples(index=False, name=None):
#     ws.append(row)
#
# # --------------------------
# # 4. Create Pie Chart
# # --------------------------
# pie = PieChart()
# pie.title = "Monthly Sales Distribution"
#
# # Data range (Sales column)
# data = Reference(ws, min_col=2, min_row=1, max_row=len(df) + 1)
#
# # Categories (Month column)
# cats = Reference(ws, min_col=1, min_row=2, max_row=len(df) + 1)
#
# pie.add_data(data, titles_from_data=True)
# pie.set_categories(cats)
#
# # Optional – Make chart bigger
# pie.width = 14
# pie.height = 10
#
# # --------------------------
# # 5. Insert chart into Excel
# # --------------------------
# ws.add_chart(pie, "E5")
#
# # --------------------------
# # 6. Save File
# # --------------------------
# wb.save("sales_pie_chart.xlsx")
#
# print("Excel with Pie Chart Created: sales_pie_chart.xlsx")
