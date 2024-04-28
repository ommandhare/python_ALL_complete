path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\sqlGen\configForSql.csv"
factDict = {'b':"sum(fact)","a":"sum(fact),min(fact),max(fact)"}
cnt=0
for line in open(path):
    if(cnt==0):
        cnt +=1
        continue
    print(line,end="")
    table_name,dimensions,timeDim,facts,factCd = line.strip().split(",")
    dimList = dimensions.split("#")
    factList = facts.split("#")
    for fact in factList:
        code = factDict[factCd]
        code = code.replace("fact", fact)
        print("available aggreation : ",code)
        print("\n")
    sqlStart = "SELECT "
    sqlFrom = " FROM " + table_name
    sqlGrp = " GROUP BY "
    for dim in dimList:
        print("normal select : ")
        sql = sqlStart + dim + sqlFrom+";"
        print(sql)
        print("\n")
        print("select  with aggregate functions : ")
        sql2 = sqlStart + dim +","+code +sqlFrom + sqlGrp + dim + ";"
        print(sql2)
        print("\n")
        print("\n")


