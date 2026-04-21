from openpyxl import Workbook
from openpyxl.chart import PieChart,BarChart,BarChart3D, Reference

# Create a workbook and select the active sheet
wb = Workbook()
ws = wb.active

# Add some data
data = [
    ['Month', 'Sales'],
    ['Jan', 40],
    ['Feb', 60],
    ['Mar', 80],
    ['Apr', 20],
]
for row in data:
    ws.append(row)

# Create a bar chart
chart = BarChart3D()
chart.title = "Monthly Sales"
chart.x_axis.title = "Month"
chart.y_axis.title = "Sales"

# Define data and categories for chart
data = Reference(ws, min_col=2, min_row=1, max_row=5)
cats = Reference(ws, min_col=1, min_row=2, max_row=5)
chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)

# Add chart to sheet
ws.add_chart(chart, "E5")

# Save file
wb.save("sales_chart.xlsx")
