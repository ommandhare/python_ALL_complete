
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

typeDict={'int':'INT','str':'VARCHAR(50)','date':'DATE'}
contDict={'not null':'NOT NULL','primary key':'PRIM'}

for tableName,cols in tableDict.items():
    sqlStart='CREATE TABLE '+tableName+' ( '
    primaryKey=[]
    sqlEnd =')\n'
    for col in cols:
        if(col[2]=='primary key'):
            sqlStart+=col[0]+' '+col[1]+' , '
            primaryKey.append(col[0])
        else:
            sqlStart+=col[0]+' '+col[1]+' '+col[2]+ ' , '
    if(len(primaryKey)!=0):
        sqlStart+='PRIMARY KEY('
        for pCol in primaryKey:
            sqlStart+=pCol+' , '
        sqlStart+=') '
    sqlStart+=sqlEnd
    sqlStart=sqlStart.replace(', )',')')
    for type in typeDict:
        sqlStart=sqlStart.replace(' '+type+' ',' '+typeDict[type]+' ')
    for cont in contDict:
        sqlStart=sqlStart.replace(' '+cont+' ',' '+contDict[cont]+' ')

    print(sqlStart)





