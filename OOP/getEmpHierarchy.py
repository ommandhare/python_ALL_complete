import employee as e
path = r'C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\OOP\empRecord.csv'
count=0
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
id=12
eObj = companyRecDict[id]
print("EMP HIERARCHY FOR: ",id)
count=0
while(id!=-1000):
    empObj=companyRecDict[id]
    if(count==0):
        print(empObj.name,end="")
        count+=1
    else:
        print("-->",empObj.name,end="")
    mgr = empObj.manager_id
    id = mgr