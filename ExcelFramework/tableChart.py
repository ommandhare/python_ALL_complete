import pandas as pd
import formatConfig as fcg
from openpyxl import Workbook
from openpyxl.chart import PieChart, BarChart, BarChart3D, Reference
import numpy as np
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side

templatePath = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\ExcelFramework\template.csv"
path = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\ExcelFramework\sampleData.csv"
outPath = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\ExcelFramework\TemplateOutput.xlsx"

# STEP 1::: READ Cfg FILE AND CREATE A VAR VAL DICT
df = pd.read_csv(path)
# print(df.values)
varValDict = {}
count = 0
for line in open(templatePath):
    if (count == 0):
        count += 1
        continue
    print(line)
    file, wsheet, obj, oName, variable, value, type = line.strip().split(",")
    key = file + "_" + wsheet + "_" + oName + "_" + variable
    vValue = value
    if (type == 'i'):
        varValDict[key] = int(vValue)
    else:
        varValDict[key] = vValue
print(varValDict)

# STEP 2::: READ MAIN DATA FRAME OF THE WORKSHEET
## in this case main data frame is sec2
# Save to Excel as a real Excel Table
with pd.ExcelWriter(outPath, engine='xlsxwriter') as writer:

    # Correct variable definitions
    startRowPandas = varValDict['f1_w1_sec2_sec_st_row'] + 1
    startColPandas = varValDict['f1_w1_sec2_sec_st_col']

    # Correct df.to_excel()
    df.to_excel(
        writer,
        sheet_name=varValDict['f1_w1_sheet_name'],
        startrow=startRowPandas,
        startcol=startColPandas,
        header=False,
        index=False
    )

    workbook = writer.book
    worksheet = writer.sheets[varValDict['f1_w1_sheet_name']]
    # data_ws.freeze_panes(5, 4)

    # =======================================================
    # XLSXWRITER BAR CHART (NO ERRORS)
    # =======================================================

    chart = workbook.add_chart({'type': 'column'})

    df_start_row = startRowPandas  # where df data starts
    df_start_col = startColPandas
    max_r, max_c = df.shape

    # Add series with categories and values
    chart.add_series({
        'city': 'Price',
        'categories': [
            worksheet.name,
            df_start_row + 1,  # First data row
            df_start_col,  # Category column (Name)
            df_start_row + 10,
            df_start_col
        ],
        'values': [
            worksheet.name,
            df_start_row + 4,
            df_start_col + 4,  # Values column (Price)
            df_start_row + 10,
            df_start_col + 4
        ]
    })

    # Set titles
    chart.set_title({'name': 'Population'})
    chart.set_x_axis({'name': 'Name'})
    chart.set_y_axis({'name': 'Population'})

    # Insert chart on sheet
    worksheet.insert_chart('K10', chart)


