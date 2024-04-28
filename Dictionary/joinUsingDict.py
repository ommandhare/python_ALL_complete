pathDim = r"C:\PythonWork\Data\test\student_dim.csv"
pathFact = r"C:\PythonWork\Data\test\result_fact.csv"
studentDict = {}
count=0
for line in open(pathDim):
    if(count==0):
        count +=1
        continue
    print(line,end="")
    id,fName,lName = line.strip().split(",")
    id = int(id)
    name = fName + "_" + lName
    studentDict[id] = name


print(studentDict)

count=0
for line in open(pathFact):
    if(count==0):
        count +=1
        continue
    #print(line,end="")
    id,eng,math,chem,phy,bio,pct,cls = line.strip().split(",")
    id = int(id)
    if(id in studentDict):
        name = studentDict[id]
        print("ID: ",id,\
               ",NAME: ",name,\
               ",PCT: ",pct,\
               ",CLASS: ",cls)

### join using list is n square complexity algorithm