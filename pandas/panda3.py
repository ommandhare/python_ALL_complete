import pandas as pd
#import numpy as np
"""
def area_of_circle(radius,pi):
    return pi*radius*radius

## fixed no of arguments and 
## order of arguments is to be followed in toto 
## to be able to get correct answers
#area = area_of_circle(3.14,3)

def test(param2,param1,param3):
    
    param1 = param2 + param1 * param3
    return param1

######## LOAD CSV FILES ::::::::::::::
# with header
#df1 = pd.read_csv("test.csv")
#print(df1)

"""
#without header
df1 = pd.read_csv("test1.csv",usecols=[2,3], header=None)
print(df1)

#with custome header
df1 = pd.read_csv("test1.csv", header=None,names=["name","weight","age","height"], usecols=[0,1,2,3])
print(df1)
"""

#### Give list of values to be considered as na values
print("******************** NA VALUE LIST *******************")
df2 = pd.read_csv("test2.csv",header=None, na_values = ["?","_","","...."])
print(df2)

df2.dropna(inplace=True)
print("DROP NA ROWS")
print(df2)
########################### Drop rows if selected columns have na values ###########################
df2 = pd.read_csv("test2.csv", header=None, names=["name","weight","age","height"],na_values = ["?", "_"])
print("&*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
print(df2)
print("%$%$$$$$%$%$%$%$%$%$%$%$$$$%$%$%$%$%$%$%$%$%$%$%$%$")
df2.dropna(inplace=True, subset=['age','name'])
print("DROP NA IF AGE HAS NA OR NAME has NA")
print(df2)


#################### FILL NA VALUES #######################
print("print na values with default value: say 0")

df3 = pd.read_csv("test2.csv", header=None, names=["name","weight","age","height"],na_values = ["?", "_"])
print(df3)
df4 = df3.fillna(0)
print("********************* after fill na 0 ****************")
print(df4)
print("same in place")
df3.fillna(0, inplace=True)
print(df3)

##### replace nulll values for different columns separately ################
df = pd.read_csv("test2.csv", header=None, names=["name","weight","age","height"],na_values = ["?", "_"])
values = {'age':30, 'height':5.0,'name':'bandya'}
df5 = df.fillna(value=values)
print(df5) 

print("*****************FFILL START ******************")
df = pd.read_csv("test2.csv", header=None, names=["name","weight","age","height"],na_values = ["?", "_"])
print(df)
df_bfill = df.fillna(method='bfill')
print(df_bfill)
df_fill = df.fillna(method='ffill')
print(df_fill)



"""
print("********************JOINS************************")
########################## JOINS #############################################
df = pd.read_csv("testJoin.csv", na_values = ["?", "_"])
print(df)
df_sal = pd.read_csv("test_merge.csv",header=None, names=['nm','salary'])
print(df_sal)
print("inner join")
df_joined = pd.merge(df,df_sal, left_on='name', right_on='nm')
print(df_joined)

print("left outer")
df_left_outer = pd.merge(df,df_sal, left_on='name', right_on='nm', how='left')
print(df_left_outer)
print("right_outer")
df_right_outer = pd.merge(df,df_sal, left_on='name', right_on='nm', how='right')
print(df_right_outer)

print("full_outer")
df_full_outer = pd.merge(df,df_sal, left_on='name', right_on='nm', how='outer')
print(df_full_outer)




