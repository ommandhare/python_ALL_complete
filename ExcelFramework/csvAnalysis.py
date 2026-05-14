import pandas as pd
import formatConfig as fcg





# params:  baseWordPath, start_row, start_col
def data_sheet(path, data_name, startrow, startcol, filter):
    df = pd.read_csv(path)

    df.to_excel(writer, sheet_name=data_name, index=False, startrow=startrow)

    ws = writer.sheets[data_name]

    # Data boundaries
    first_data_row = startrow + 1
    last_data_row  = startrow + len(df)
    first_col = startcol
    last_col = startcol + len(df.columns) - 1

    # Add table
    ws.add_table(
        startrow,
        startcol,
        last_data_row,
        last_col,
        {
            "style": fcg.tableStyleDict[varValDict['f1_w1_sec2_tableStyle']],
            "columns": [{"header": col} for col in df.columns],
            "autofilter": filter
        },
    )
    ws.hide_gridlines(2)
    # Return worksheet + boundaries
    return df, ws, first_data_row, last_data_row, first_col, last_col

def summarize(df, category_col, value_col):
    """
    Summarizes data for pie chart usage.
    Returns a grouped dataframe with:
        category_col, aggregated values
    """
    summary_df = (
        df.groupby(category_col)[value_col]
        .sum()
        .reset_index()
        .sort_values(value_col, ascending=False)
    )
    return summary_df, category_col, value_col


def pie_chart(title, a, b, legend, df_summarize):
    Pie_Chart_sheet = title
    workbook.add_worksheet(Pie_Chart_sheet)
    pie_ws = writer.sheets[Pie_Chart_sheet]
    pie_ws.hide_gridlines(2)

    chart = workbook.add_chart({'type': 'pie'})

    # Column indexes in summarized df (df_summarize)
    cat_idx = df_summarize.columns.get_loc(a)
    val_idx = df_summarize.columns.get_loc(b)

    # Data starts at row 1 in Excel
    first_data_row = 1
    last_data_row = len(df_summarize)

    # Write summarized df into sheet "Product_Data_PIE"
    # sheet_data_name = "Pie_Data_" + title
    df_summarize.to_excel(writer, sheet_name=Pie_Chart_sheet, index=False)

    # Colors from formatConfig
    pie_color_key = varValDict.get("f1_w1_pie1_pie", "vibrant")
    color_points = fcg.pieColorSets[pie_color_key]["points"][: len(df_summarize)]

    chart.add_series({
        'name': legend,
        'categories': [Pie_Chart_sheet, first_data_row, cat_idx, last_data_row, cat_idx],
        'values':     [Pie_Chart_sheet, first_data_row, val_idx, last_data_row, val_idx],
        'points':     color_points
    })

    chart.set_title({'name': legend})
    chart.set_style(10)

    pie_ws.insert_chart('F5', chart, {
        'x_scale': 1.4,
        'y_scale': 1.4
    })

def bar_chart_sum(title, a, b, legend, df_summarize):
    """
    title       -> sheet name for this bar chart
    a           -> category column name in df_summarize
    b           -> value column name in df_summarize
    legend      -> series name
    df_summarize-> grouped/aggregated dataframe
    """

    sheet_name = title

    # Write summarized data to this sheet
    df_summarize.to_excel(writer, sheet_name=sheet_name, index=False)

    bar_ws = writer.sheets[sheet_name]
    bar_ws.hide_gridlines(2)

    chart = workbook.add_chart({'type': 'column'})

    # Column indexes
    cat_idx = df_summarize.columns.get_loc(a)
    val_idx = df_summarize.columns.get_loc(b)

    first_data_row = 1
    last_data_row = len(df_summarize)

    chart.add_series({
        'name': legend,
        'categories': [sheet_name, first_data_row, cat_idx, last_data_row, cat_idx],
        'values':     [sheet_name, first_data_row, val_idx, last_data_row, val_idx],
    })

    bar_ws.insert_chart('F5', chart, {
        'x_scale': 2.0,
        'y_scale': 1.5
    })

def pivot_table(
    writer,
    df,
    sheet_name,
    index_cols,
    value_cols,
    aggfunc="sum",
    columns=None,
    fill_value=0,
    table_style_key="SM2"
):
    """
    Generate a pivot table with multiple rows, columns and values.

    Parameters
    ----------
    writer : pd.ExcelWriter
        Active Excel writer

    df : pd.DataFrame
        Source dataframe

    sheet_name : str
        Excel sheet name

    index_cols : list
        Row fields (e.g. ["category", "brand"])

    value_cols : list
        Value fields (e.g. ["qty", "price"])

    aggfunc : str or dict
        Aggregation function ("sum", "mean", etc.)

    columns : list or str, optional
        Column fields (e.g. "region")

    fill_value : int or float
        Replace NaN values

    table_style_key : str
        Key from formatConfig.tableStyleDict
    """

    # -----------------------------
    # 1️⃣ Create Pivot DataFrame
    # -----------------------------
    pivot_df = pd.pivot_table(
        df,
        index=index_cols,
        columns=columns,
        values=value_cols,
        aggfunc=aggfunc,
        fill_value=fill_value
    )

    # -----------------------------
    # 2️⃣ Flatten MultiIndex Columns
    # -----------------------------
    pivot_df.columns = [
        "_".join(map(str, col)).strip()
        if isinstance(col, tuple) else col
        for col in pivot_df.columns
    ]

    pivot_df = pivot_df.reset_index()

    # -----------------------------
    # 3️⃣ Write to Excel
    # -----------------------------
    pivot_df.to_excel(writer, sheet_name=sheet_name, index=False)

    ws = writer.sheets[sheet_name]
    ws.hide_gridlines(2)

    # -----------------------------
    # 4️⃣ Apply Excel Table Style
    # -----------------------------
    start_row = 0
    start_col = 0
    end_row = len(pivot_df)
    end_col = len(pivot_df.columns) - 1

    ws.add_table(
        start_row,
        start_col,
        end_row,
        end_col,
        {
            "style": fcg.tableStyleDict[table_style_key],
            "columns": [{"header": c} for c in pivot_df.columns],
        },
    )

    return pivot_df




templatePath = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\ExcelFramework\template.csv"
path = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\ExcelFramework\product.csv"
outPath = r"C:\Users\Om Mandhare\PycharmProjects\python_ALL_complete\ExcelFramework\csvAnalysis.xlsx"


data=pd.read_csv(path)

print(data)

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




with (pd.ExcelWriter(outPath, engine='xlsxwriter') as writer):

    workbook = writer.book

    # Data table (formatted)
    df, data_ws, first_data_row, last_data_row, first_col, last_col = \
    data_sheet(path,"Product_Data",0,0,True)


    # Summarize
    df_summarize,category_col, value_col = summarize(df, "category", "qty")

    # Bar Chart
    bar_chart_sum("BAR_Qty_by_Category", category_col, value_col, "Qty by category", df_summarize)

    # Pie Chart using summarized df
    pie_chart("PIE", category_col, value_col, "Qty by category", df_summarize)

    pivot_df = pivot_table(
        writer=writer,
        df=df,
        sheet_name="Pivot_Category_Brand",
        index_cols=["category"],
        value_cols=["qty", "price"],
        aggfunc="count"
    )
