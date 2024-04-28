path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\sqlGen\createTable.csv"
with open(path) as ct:
    typeDict={'int':'INT','str':'VARCHAR(50)','date':'DATE'}
    conDict={'p':'PRIMARY KEY','nn':'NOT NULL','na':''}
    cnt = -1
    for line in ct:
        if(cnt == -1):
            cnt+=1
            continue
        tableName,dim,dimType,dimCon=line.strip().split(",")
        #print(f"table:{tableName},dim:{dim} \n types:{dimType} constrint: {dimCon}")
        dimList=dim.split("#")
        dimTypeList=dimType.split('#')
        conList=dimCon.split('#')

        sqlStart='CREATE TABLE '+tableName+"("
        sqlEnd  =');'

        for idx in range(len(dimList)):
            sqlStart+=dimList[idx]+' '+dimTypeList[idx]+' '+conList[idx]+' ,'
        sqlStart+=sqlEnd

        for types in typeDict:
            sqlStart=sqlStart.replace(' '+types+' ',' '+typeDict[types]+' ')

        for con in conDict:
            sqlStart=sqlStart.replace(' '+con+' ',' '+conDict[con]+' ')
        sqlStart=sqlStart.replace(',);',');')

        print(sqlStart)