"""
read employee manager file build employee class and
define class variable employee count and check working of class variable

"""


import employee as e
path = r'C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\OOP\empRecord.csv'

empRec=[]
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
        empRec.append(tempEmp)


print("CLASS VARIABLE")
print(e.Employee.counEmployees)

