"""
read employee manager file to build employee-manager tree and
findout nearest common manager for any two employees given by user.

"""

import employee as e
path = r'C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\OOP\empRecord.csv'

def getManagerList(id,list):
    count = 0
    if id in TreeDict:
        print("found")
        print("EMP HIERARCHY FOR :: ", id)
        while (id != -1000):
            eobj = TreeDict[id]
            if (count == 0):
                print(eobj.name, end="")
                count += 1
            else:
                print(" ==>", eobj.name, end="")
                list.append(eobj.name)
            mgr = eobj.manager_id
            id = mgr
    else:
        print("ID NOT FOUND TRY OTHER ONE")


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
#
id1=int(input("Enter the ID 1 for finding TREE :::::"))
mList1=[]
getManagerList(id1,mList1)
print("LIST OF MANAGER 1")
print(f"First list", mList1)

print("####################################################")

id2=int(input("Enter the ID 2  for finding TREE :::::"))
mList2=[]
getManagerList(id2,mList2)
print("LIST OF MANAGER 2")
print("Second list",mList2)



print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("COMMON MANAGERS of both ids")
for i in mList1:
    for j in mList2:
        if (i==j):
            print(i)