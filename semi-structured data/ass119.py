"""
read json file and print all lines, search specific tags
"""

import json


path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\semi-structured data\json2.json"

def dictRecurssion(dataDict,level):
    #browse over this level to check if any dict is present
    flag=0
    for k,v in dataDict.items():
        for i in range(level):
            print("---",end="")
        print("KEY: ",k," AT LEVEL: ",level,end="")
        print(" VALUE TYPE: ",type(v))
        if(type(v)==dict):
            flag=1
    if(flag==1):
        for i in range(level):
            print("---", end="")
        print("Lets go to next level")
    for k,v in dataDict.items():
        if(type(v)==dict):
            for i in range(level):
                print("---", end="")
            print("RECURSSION FOR KEY: ",k)
            dictRecurssion(v,level+1)



with open(path) as f:
    data=json.load(f)

print(data)

print("dict_recursion")
print("##############")
level=0
dictRecurssion(data,level)


searchTag=input(print("enter tag to search : "))

if searchTag in data:
    print("Tag Found")

