import pandas as pd
import numpy as np
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side



path = r"C:\Philomath\sampleData.csv"
outPath = r"C:\Philomath\OutPutFormat2711.xlsx"

df = pd.read_csv(path)
print(df.values)


# Save to Excel as a real Excel Table
with pd.ExcelWriter(outPath, engine='xlsxwriter') as writer:
    # Write the data to Excel, starting at row 1 (to leave space for table headers)
    df.to_excel(writer, sheet_name='TD', startrow=5,startcol=2, header=False, index=False)

    # Access the workbook and data_ws objects
    workbook  = writer.book
    worksheet = writer.sheets['TD']
    worksheet.auto_filter_ref = None
    worksheet.freeze_panes(5,4)

    # Define the table header (column names)
    column_settings = [{'header': col} for col in df.columns]

    # Define the table range
    (max_row, max_col) = df.shape
    stRow = 4
    stCol = 2
    worksheet.add_table(stRow, stCol, max_row+4, max_col + 1, {
        'columns': column_settings,
        'name': 'MyExcelTable',  # Optional: Name your table
        'style': 'Table Style Medium 10'  # Optional: Choose table style
    })
    merge_format = workbook.add_format({
        'bold': True,
        'bg_color': '#00008B',  # Dark Blue
        'font_name': 'Calibri',  # Font family
        'font_size': 32,
        'font_color': 'white',  # Optional: make text visible
        'align': 'center',
        'valign': 'vcenter',
        'border': 1
    })
    worksheet.merge_range(1,2,2,max_col+1,'merged_header',merge_format)

