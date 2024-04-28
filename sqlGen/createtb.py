path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\createTable.csv"
tableDict = {}
with open(path) as ct:
    cnt=-1
    for line in ct:
        if(cnt == -1):
            cnt+=1
            continue
        tableName,col,dType,colType,cont=line.strip().split(",")
        if(tableName not in tableDict):
            tableDict[tableName]=[[col,dType,cont]]
        else:
            tableDict[tableName].append([col,dType,cont])


print(tableDict)

typeDict={'int':'INT','str':'VARCHAR(50)','date':'DATE'}
contDict={'not null':'NOT NULL','primary key':'PRIM'}