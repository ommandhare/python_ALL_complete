"""
build employee-manager tree using  and findout hierarchy for any given employee.
For example if user gives "Pranav" as input,
findout all managers of Pranav till top boss.
Sample output: Pranav ==> Mandar ==> Soham ==> Ishan ==> Swati ==> Saurabh

"""

import employee as e
path = r'C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\OOP\empRecord.csv'

TreeDict={}
count=0
for line in open(path):
    if count==0:
        count+=1
        continue
    else:
        # print(line, end="")
        a, fName, lName, age, ht, sal, t = line.strip().split(",")
        id = int(a)
        age = int(age)
        ht = float(ht)
        sal = float(sal)
        mgr = int(t)
        tempEmp = e.Employee(id, fName + " " + lName, age, ht, sal, mgr)
        TreeDict[id] = tempEmp

print(TreeDict)

id=int(input("Enter the ID for finding TREE :::::"))

count=0
if id in TreeDict:
    print("found")
    print("EMP HIERARCHY FOR :: ", id)
    while(id!=-1000):
       eobj=TreeDict[id]
       if (count==0):
           print(eobj.name,end="")
           count+=1
       else:
           print(" ==>",eobj.name,end="")
       mgr=eobj.manager_id
       id=mgr
else:
    print("ID NOT FOUND TRY OTHER ONE")