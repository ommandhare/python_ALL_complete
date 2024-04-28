import pandas as pd
import numpy as np
import config as cfg
"""
######## LOAD CSV FILES ::::::::::::::
# with header
df1 = pd.read_csv("test.csv")
print("PRINT TEST.CSV.... this file has header")
print(df1)

#without header
print("PRINT TEST1.CSV.. this file doesn't have header.. \nPANDAS is reading only two columns from this file")
df1 = pd.read_csv("test1.csv", header=None, usecols=[2,3])
print(df1)
"""
#with custome header
print("PRINT TEST1.csv .. this file doesn't have header, assign custom header given by user (column_names)")
df1 = pd.read_csv("test1.csv", header=None,names=["name","weight","age","height"], usecols=[0,1,2,3])
print(df1)

################ slicing and dicing ###########################
#### what is slicing and Dicing:
#### selecting part of the data that we need.
#### how slicing and dicing is done in sql?
#### Slicing and Dicing is done in SQL using: 
#### Select clause (select all or partial columns) and 
#### Where clause (where clause will help selecting all or partial rows)

df_name = df1.name
print("NAMES: ")
print(df_name)


df_name1 = df1['name']
print(df_name1)
#### data frame is two dimensional array
#### that means if i give two dimensions i will access one cell.
#### df1[1,1]
#### iloc function uses indexes to refer to columns and rows
#### when there are 100s of columns and 1000s rows.. using idexes is tricky
print("second row, first column")
print(df1.iloc[2,1])
print("second row using index")
r2 = df1.iloc[2,]
print(df1.iloc[2,])
print("type of complete dataframe: ", type(df1))
print(type(r2))

print("second column using index")
df_col = df1.iloc[:,2]
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@TYPE OF 2nd Col DF: ", type(df_col))
print(df_col)
print(df1.iloc[:,2])

print("SLICE BY ROWS-------------------------------------------------------------")
df_rows = df1[2:4]
print(df_rows)

print("SLICE BY COLUMNS")
df_col = df1[["name","age","weight"]]
print(df_col)

#### slicing by  index locations
print("SLICING BY INDEX LOCATION ")
df_iloc = df1.iloc[3:5,[0,2]]
print(df_iloc)
df_iloc1 = df1.iloc[1:3,[1,2,3]]
print(df_iloc1)

#### all rows selected column
print("ALL ROWS SELECTED COLUMN")
df_sc = df1.loc[:,["name","age"]]
print(df_sc)

#### all columns selected row
print("\n\nALL COLUMNS SELECTED ROW")
df_sr = df1.loc[1:2]
print(df_sr)
"""
"""
#a[10][10]
# a[3][3]
# a[3] --- 4 row all columns

### filtering data
### filter using one value
print("\n\n FILTER USING ONE VALUE----====================<<<<>>>>>>>>>>>>>>>>>>>")
df_flt = df1[df1.age<40]
print(df_flt)

df_flt1 = df1[df1.age == 43]
print(df_flt1)

### filter with list of values
### in clause in sql -- select * from tran where item_id in (1,2,3,87)
print("\n\n FILTER WITH LIST OF VALUES: ")
df_fltlist = df1[df1['age'].isin([34,38,44])]
print(df_fltlist)
### difference between list and tuple
##### difference between iloc and loc ==> iloc is index location (array) where as loc is index location pandas df
### assignments
print("\n\n Assignments")
df1.loc[3,["age"]] = 101
print(df1)

df1.loc[2,["age"]] = np.nan
print(df1)


### add new column to dataframe with a hard coded value
df1["mycol"] = 100
df1["col_name_wtHt"] = df1.weight * df1.height
print(df1)

print(df1.columns)
a = [[1,2]]
c = a*3
print(c)
###### assignment
# one column or one row is one data series -- array
df1["new_col"] = np.array(["abc"] * len(df1))
print(df1)

#### rename column
print("TEETEETETETETEST>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
df1.rename(columns={"new_col":"my_new_col","height":"007"},inplace=True)
print(df1)
print("Existing name of the columns in pandas dataframe ************************")
print(df1.columns)

df1.columns = cfg.final_column_name_list
print("NEW COL LIST: ", cfg.final_column_name_list)
print(df1)
#### write to csv
### how to write file without index
df1.to_csv("test_out_df9_26.csv")


