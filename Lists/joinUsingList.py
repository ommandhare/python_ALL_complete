pathDim = r"C:\PythonWork\Data\test\student_dim.csv"
pathFact = r"C:\PythonWork\Data\test\result_fact.csv"
studentList = []
count=0
for line in open(pathDim):
    if(count==0):
        count +=1
        continue
    print(line,end="")
    id,fName,lName = line.strip().split(",")
    id = int(id)
    name = fName + "_" + lName
    studentRec = [id,name]
    studentList.append(studentRec)

print(studentList)
count=0
for line in open(pathFact):
    if(count==0):
        count +=1
        continue
    #print(line,end="")
    id,eng,math,chem,phy,bio,pct,cls = line.strip().split(",")
    id = int(id)
    for sRec in studentList:
        if(id==sRec[0]):
            print("ID: ",id,\
                   ",NAME: ",sRec[1],\
                   ",PCT: ",pct,\
                   ",CLASS: ",cls)
            break ## there may be case when we want to
                  ## get all joining rows out


### join using list is n square complexity algorithm