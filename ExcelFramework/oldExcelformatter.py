import pandas as pd
import formatConfig as fcg
from openpyxl import Workbook
from openpyxl.chart import PieChart,BarChart,BarChart3D, Reference
import numpy as np
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side


templatePath = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\ExcelFramework\template.csv"
path = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\ExcelFramework\sampleData.csv"
outPath = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\ExcelFramework\TemplateOutput.xlsx"

# STEP 1::: READ Cfg FILE AND CREATE A VAR VAL DICT
df = pd.read_csv(path)
#print(df.values)
varValDict = {}
count=0
for line in open(templatePath):
    if(count==0):
        count+=1
        continue
    print(line)
    file,wsheet,obj,oName,variable,value, type = line.strip().split(",")
    key = file +"_" + wsheet + "_" + oName + "_" + variable
    vValue = value
    if(type=='i'):
        varValDict[key] = int(vValue)
    else:
        varValDict[key] = vValue
print(varValDict)

# STEP 2::: READ MAIN DATA FRAME OF THE WORKSHEET
## in this case main data frame is sec2
# Save to Excel as a real Excel Table
with pd.ExcelWriter(outPath, engine='xlsxwriter') as writer:
    # Write the data to Excel, starting at row 1 (to leave space for table headers)
    ## only pandas dataframe row index starts at 1 and column index starts at 0
    startRowPandas = varValDict['f1_w1_sec2_sec_st_row'] + 1
    ## all other cases all indices start at 0
    df.to_excel(writer, sheet_name=varValDict['f1_w1_sheet_name'],
                startrow=startRowPandas,
                startcol=varValDict['f1_w1_sec2_sec_st_col'],
                header=False, index=False)
    #
    # Access the workbook and data_ws objects

    workbook = writer.book
    # newSheet = workbook.add_worksheet("bar chart")
    worksheet = writer.sheets[varValDict['f1_w1_sheet_name']]
    worksheet.auto_filter_ref = False
    worksheet.freeze_panes(5,4)


    # Define the table header (column names)
    column_settings = [{'header': col} for col in df.columns]
    print(column_settings)
    # Define the table range
    (max_row, max_col) = df.shape
    # print("MAX ROW::: ", max_row,"\nMAX COL: ",max_col)

    #max_col + 1
    worksheet.add_table(varValDict['f1_w1_sec2_sec_st_row'],
                        varValDict['f1_w1_sec2_sec_st_col'],
                        max_row+4,max_col+1 , {
        'columns': column_settings,
        'name': 'MyExcelTable',  # Optional: Name your table
        'style': fcg.tableStyleDict[varValDict['f1_w1_sec2_tableStyle']]  # Optional: Choose table style
    })
    worksheet.auto_filter_ref = False



    ## file 1, data_ws 1, section 1
    sec1_format = workbook.add_format(fcg.formatStyle[varValDict['f1_w1_sec1_format']])
    worksheet.merge_range(varValDict['f1_w1_sec1_sec_st_row'],
                          varValDict['f1_w1_sec1_sec_st_col'],
                          varValDict['f1_w1_sec1_sec_end_row'],
                          max_col+1,'merged_header',
                          sec1_format)


