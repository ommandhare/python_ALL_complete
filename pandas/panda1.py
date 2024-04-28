import pandas as pd
import config as cfg


# select name, height FROM employee;
# where is data? -- mysql
# what is file format? -- mysql
# what is order of the column? -- given by user at the time of table definition
# what is data type of the column? -- given by user at the time of table definition
# what is primery key? -- given by user at the time of table definition
#for line in open("test.csv"):
 #   print(line)



##### hard coded way to populate dataframe #######

### Data Frame with Data as List of Lists
#### pd.DataFrame()

df1 = pd.DataFrame([[2,4,6],[2,4,8]])
print(df1)

#### Data Frame with Column Names
####pd.DataFrame(data,column=[],)
df1 = pd.DataFrame([[2,4,6],[2,4,8]],columns=["age","height","weight"])
print(df1)
print(df1.columns)






### functions -- input -- processing - output
### functions input::: (v1,v2,v3)
### functions input::: (list) ... it can be kwargs
### Data Frame with column and row names

df1 = pd.DataFrame([[2,4,6],[2,4,8]],index=["High","Low"],columns=["age","height","weight"])
print(df1)


### we can get information about columns of a data frame using df.columns
for col in df1.columns:
     print("PRINTING IN FOR LOOP:-- NAME OF COL: ",col)


#######################################################
### Data Frame with Data as List of Dictionaries (every row is one dictionary) -- JSON
#### Existing data structure in program can be used to create a pandas data frame

dict_names = [{"Name":"Pranav","MiddleName":"Aravind","Surname":"Kulkarni","AGE":24},{"Name":"Priyanka","Surname":"Nikam"},{"Name":"Soham","Height":5.5},{"MiddleName":"Sanjay","Surname":"Mandhare","Name":"Om","AGE":22}]
df1 = pd.DataFrame(dict_names)
print(df1)


#print(dir(df1))







######## LOAD CSV FILES ::::::::::::::
# with header
print("#$#$#$##$##$#$#$$#$#$#$#$###$#")
# test.csv is in current working directory
path = r"C:\PythonWork\DataAnalysis\test.csv"
df1 = pd.read_csv(path)
#print("DATA TYPE: ",type(df1))
print(df1)
print("COLUMN NAMES: ", df1.columns)



#without header
print("*****************HEADER = NONE ****************************")
#
path=r"C:\PythonWork\DataAnalysis\test1.csv"
df1 = pd.read_csv(path,header=None)
#df1 = pd.read_csv(path)
print(df1)
print("COLUMN NAMES BY DEFAULT (header is none): ",df1.columns)
df1.columns = ["name","weight","age","height"]
print("COLUMN NAMES AFTER ASSIGNING COLUMN NAMES: ",df1.columns)
print(df1)


#print("bring input data from config file")
#print(cfg.e_file_header)

#usecols=[2,3]
#with custome header
#usecols --- is your select clause you can select all or partial columns
#names -- names is a list of column names
#there should not be any hard-coding in your actual program.
# move all parameter values (paths, column names, column list... etc.) to
# one parameter file (can call it config.py or input.py)
# or it can be a text file or JSON file or Yaml file and name of this file and path of this file
# can be given as commadn line argument
path=r"C:\PythonWork\DataAnalysis\test11.csv"
df1 = pd.read_csv(path, header=None,names=cfg.e_file_header1, usecols=[0,1,2,3])
print("$$$$$$$$$$$$ header none, custome column names, user_col = all columns")
print(df1)
print(" COLUMNS IN THIS DATA FRAME df1::: ", df1.columns)

# select name from df1;
df_name = df1.name
"""
"""
#print(df_name)

### projection -- select clause and filters are to be applied first.
### hard codeing only at one place (config files)
print("SELECT ONLY FEW COLUMNS FROM THE FILE")
df2 = pd.read_csv("test11.csv", header=None,names=["name","height"], usecols=[0,3])
print(df2)

### head and tail. --> similar to limit clause in SQL it helps us understand how data looks
### wt   name  age height
### 3333 xyztt 54 2.3
print("\n","first 2 rows")
df1_head = df1.head(2)
print(df1.head(2))

print("\n","last one row")
print(df1.tail(1))


### get data types, columns,  values, index etc.
print("COLUMNS")
print(df1.columns)

print("\n","INDEX")
print(df1.index)

print("\n","DATA TYPES")
print(df1.dtypes)

print("\n","VALUES")
print(df1.values)
print(type(df1.values))

print("****************************************************")
print(df1.describe())
"""
##### find function is to search in strings
str1 = "Welcome to python and SqL"
idx = str1.find("python")
print("python found at index: ", idx)

### get columns from user and print only those columns
#columns = input("Enter column names separated by comma:")
userColList="height,weight"
print(":::::::::::::::::::::####### Value of inColumns::::::::########",userColList)
for col in df1.columns:
     print("COL IN DF: ",col)
     idx = userColList.find(col)
     print("VALUE OF IDX: ",idx)
     if( idx != -1):
          print("column found------------------------: ",col)
     else:
          print("column not found: ", col)
####### GET Statistical summary of data
print("#####$$$$$$$$$$$$$$$$$$$$$$$$$$$$##################################################$$$$$$$$$$$$$")

# when you describe dataframe, it shows computations of following parameters (only for numeric columns)
# count, mean, stddeviation, min (0th quartile), 25% 1st quartile, 50% (2nd quartile -- median), 75% (3rd quartile)
### box plot
dfDescribeOut = df1.describe()
print(dfDescribeOut)
print("OUTPUT COLUMNS::: ", dfDescribeOut.columns)
print("OUTPUT ROWS::: ", dfDescribeOut.index)

df1 = pd.read_csv("test11.csv", header=None,names=cfg.e_file_header1, usecols=[0,1,2,3])
print(df1.index)

################### sort records ####################
print("\nSORTED DATA FRAME IN DESCENDING ORDER OF WEIGHTS")
df3 = df1.sort_values("weight", ascending=False)
print(df3)

print("\nSORTED DATA FRAME IN ASCENDING ORDER OF WEIGHTS")
df3 = df1.sort_values("weight", ascending=True)
print(df3)
print("DF 1 before sort in place ******************************************")
print(df1)

df1.sort_values("weight",ascending=False,inplace=True) ### this way is better
### you don't want to create two dataframes
print("DF1 after sort in place *********************************************")
print(df1)

###########################
print(df3.head(2))
print(df3)
print("INDEX: ",df3.index)

################ slicing and dicing ###########################
df_name = df1.name
print("NAMES: ")
print(df_name)
"""

