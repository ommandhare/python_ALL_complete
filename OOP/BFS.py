# "build employee hierarchy tree (using file employeeManager.txt)
# and write a program to traverse the tree in breadth first search"
import csv
from employee import Emp
from collections import deque
def dataExtrector(path):
    empDict={}
    empMgnDict={}
    with open(path) as f:
        data = csv.reader(f)
        next(data)
        for line in data:
            emp = Emp(int(line[0]),line[1],line[2],line[3],line[4],int(line[5]))
            empDict[emp.id]=emp
            if(emp.mId not in empMgnDict):
                empMgnDict[emp.mId]=[emp]
            else:
                empMgnDict[emp.mId].append(emp)
    return empDict,empMgnDict
"""
def IterativeBFS(empDict,empMgnDict,id,discorved):
    q=deque()
    discorved[id]=True
    q.append(id)
    while q:
        id = q.popleft()
        print(f"{empDict[id].name}",end=', ')
        empList=empMgnDict[id] if id in empMgnDict else []
        for child in empList:
            if child.id not in discorved:
                discorved[child.id]=True
                q.append(child.id)
"""

def empHearchiTravel(empDict,empMgnDict,id):
    q=deque()
    q.append(id)
    while q:
        id=q.popleft()
        print(f"{empDict[id].name}",end=',')
        if(id in empMgnDict):
            for emp in empMgnDict[id]:
                q.append(emp.id)

def main():
    path='empManager.txt'
    empDict,empMgnDict=dataExtrector(path)
    empHearchiTravel(empDict,empMgnDict,2)

if _name_ =='_main_':
 main()