import errno


def buildManagerDict(empDict,mgerDict):
    for id,obj in empDict.items():
        mgrId = obj.manager_id
        if(mgrId in mgrDict):
            empList = mgrDict[mgrId]
            empList.append(obj)
            mgerDict[mgrId]=empList
        else:
            empList=[]
            empList.append(obj)
            mgerDict[mgrId]=empList

path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\OOP\empRecord.csv"

cnt=0
empDict={}
for line in open(path):
    if(cnt==0):
        cnt+=1
        continue
    print(line,end="")
    id,sal,age,ht,sal,managerId = line.strip().split(",")
    id =int(id)
    age= int(age)
    ht =int(ht)
    sal = int(sal)
    managerId = int(managerId)
    tempemp =e.employee(id,name,age,ht,sal,managerId)
    empDict[id]=tempEmp
print("Emp Dict :",empDict)


mgrDict= {}
buildManagerDict(empDict,mgrDict)
print("Mgr dict:",mgrDict)
eId=18
if(eId in mgrDict):
    empList=mgrDict[eId]
    print("Assistants for :", eId)
    for emp in empList:
        print("ID :", emp.emp_id,"NAme :",emp.name)
else:
    print(eId," has no assistants")