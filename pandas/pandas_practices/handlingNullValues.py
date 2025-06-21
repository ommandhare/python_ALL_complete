import pandas as pd


df1 = pd.read_csv("test1.csv", header=None,names=["name","weight","age","height"], usecols=[0,1,2,3])
# print(df1)


#### Give list of values to be considered as na values
# print("******************** NA VALUE LIST *******************")
# df2 = pd.read_csv("test2.csv",header=None, na_values = ["?","_","","...."])
# print(df2)

# df2.dropna(inplace=True)
# print("DROP NA ROWS")
# print(df2)
# ########################### Drop rows if selected columns have na values ###########################
# df2 = pd.read_csv("test2.csv", header=None, names=["name","weight","age","height"],na_values = ["?", "_"])
# print("&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
# print(df2)
# print("%$%$$$$$%$%$%$%$%$%$%$%$$$$%$%$%$%$%$%$%$%$%$%$%$%$")
# df2.dropna(inplace=True, subset=['age','name'])
# print("DROP NA IF AGE HAS NA OR NAME has NA")
# print(df2)
#
#
# #################### FILL NA VALUES #######################
# print("print na values with default value: say 0")
#
# df3 = pd.read_csv("test2.csv", header=None, names=["name","weight","age","height"],na_values = ["?", "_"])
# print(df3)
# df4 = df3.fillna(0)
# print("********************* after fill na 0 ****************")
# print(df4)
# print("same in place")
# df3.fillna(0, inplace=True)
# print(df3)
#
# ##### replace nulll values for different columns separately ################
# df = pd.read_csv("test2.csv", header=None, names=["name","weight","age","height"],na_values = ["?", "_"])
# values = {'age':30, 'height':5.0,'name':'bandya'}
# df5 = df.fillna(value=values)
# print(df5)
#
print("*****************FFILL and BFILL START ******************")
df = pd.read_csv("test2.csv", header=None, names=["name","weight","age","height"],na_values = ["?", "_"])
print(df)
# df_bfill = df.bfill()
# print(df_bfill)
df_fill = df.ffill()
print(df_fill)