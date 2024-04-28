
"""
generate a list of all managers who are at level 3 in employee employee hierarchy

"""
import csv
from employee import Employee

path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\OOP\empManager.txt"
empDict = {}
empMgnDict = {}
def data_EXTRACT(path):
    with open(path) as f:
        data = csv.reader(f)
        next(data)
        for line in data:
            emp = Employee(int(line[0]), line[1], line[2], line[3], line[4], int(line[5]))
            empDict[emp.emp_id] = emp
            if (emp.manager_id not in empMgnDict):
                empMgnDict[emp.manager_id] = [emp]
            else:
                empMgnDict[emp.manager_id].append(emp)




def LEVEL(empDict,empMgnDict,emp_id,level):
    Mgn = empDict[emp_id]
    if emp_id in empMgnDict:
            print(f"{level}:{Mgn.name}")
            empList = empMgnDict[emp_id]
            for emp in empList:
             LEVEL(empDict,empMgnDict,emp.emp_id,level)
    else:

            print(f"{level}:{Mgn.name}")

    # print(empDict)


data_EXTRACT(path)
print(empMgnDict)
print(empDict)


print("AT LEVEL THREE 3")
LEVEL(empDict,empMgnDict,2,3 )


