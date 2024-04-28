"""
read employee manager file (create class and functions OOP)
and store in tree (you can built tree using dictionary)

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
