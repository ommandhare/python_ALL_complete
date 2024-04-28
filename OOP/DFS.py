# "build employee hierarchy tree (using file employeeManager.txt)
# and write a program to traverse the tree in depth first search"

import csv
from employee import Emp
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

def empHearchiTravel(empDict,empMgnDict,id,level):
    Mgn = empDict[id]
    print(f"{level}{Mgn.name}")
    empList=empMgnDict[id] if id in empMgnDict else []
    for emp in empList:
        empHearchiTravel(empDict,empMgnDict,emp.id,level+"\t")





def main():
    path='empManager.txt'
    empDict,empMgnDict=dataExtrector(path)
    empHearchiTravel(empDict,empMgnDict,2,"")

if _name_ =='_main_':
 main()