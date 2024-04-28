"""
build employee hierarchy tree (using file employeeManager.txt) and
write a program to traverse the tree in breadth first search

"""
import csv
from employee import Employee
from collections import deque

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



def emp_BFS(empDict,empMgnDict,emp_id):
    q = deque()
    q.append(emp_id)
    while q:
        id = q.popleft()
        print(f"{empDict[id].name}", end=',')
        if (id in empMgnDict):
            for emp in empMgnDict[id]:
                q.append(emp.emp_id)


data_EXTRACT(path)
print(empMgnDict)
print(empDict)


print("##############################")
print("BFS TREE")
emp_BFS(empDict,empMgnDict,16)



