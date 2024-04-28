from OOP import employee as e
path = r'C:\PythonWork\Data\empRecord.csv'
count=0
def printHierarchy(id,empDict,lvl):
    if(id==-1000):
        return
    else:
        empObj = empDict[id]
        if(lvl==0):
            print(empObj.name,end="")
        else:
            print("-->",empObj.name,end="")
        printHierarchy(empObj.manager_id,empDict,lvl+1)

#companyRec = []
companyRecDict = {}
for line in open(path):
    if(count==0):
        count +=1
        continue
    print(line,end="")
    a,fName,lName,age,ht,sal,t = line.strip().split(",")
    id = int(a)
    age = int(age)
    ht = float(ht)
    sal = float(sal)
    mgr = int(t)
    tempEmp = e.Employee(id,fName+" "+lName,age,ht,sal,mgr)
    #companyRec.append(tempEmp)
    companyRecDict[id] = tempEmp
print(companyRecDict)
#print(tempEmp)
id=26
printHierarchy(id,companyRecDict,0)