import employee as e
#wrire a function to browse over emp Dictionary and build manager Dict
# this manager dict keeps manager id and list of assistents of that manager

def buildManagerDict(empDict,mgrDict):
    for id,obj in empDict.items():
        mgrId = obj.manager_id
        if(mgrId in mgrDict):
            empList = mgrDict[mgrId]
            empList.append(obj)
            mgrDict[mgrId] = empList
        else:
            empList = []
            empList.append(obj)
            mgrDict[mgrId] = empList


path = r'C:\PythonWork\Data\empManager.txt'
cnt=0
empDict = {}
for line in open(path):
    if(cnt==0):
        cnt +=1
        continue
    print(line,end="")
    id,name,age,ht,sal,managerId = line.strip().split(",")
    id = int(id)
    age = int(age)
    ht = float(ht)
    sal = float(sal)
    managerId = int(managerId)
    tempEmp = e.Employee(id,name,age,ht,sal,managerId)
    empDict[id] = tempEmp
print("EMP DICT: ",empDict)
##
mgrDict ={}
buildManagerDict(empDict,mgrDict)
print("MGR DICT: ",mgrDict)
## find assistants for  an employee
eId = 18
if(eId in mgrDict):
    empList = mgrDict[eId]
    print("ASSISTANTS FOR: ",eId," :AS GIVEN BELOW: ")
    for emp in empList:
        print("ID: ",emp.emp_id," NAME: ",emp.name)
else:
    print(eId," - has no assistents")