"""
build small application to query json file

"""

import json

path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\semi-structured data\json2.json"

with open(path) as f:
    data=json.load(f)

print(data)


findKey=input(print("enter the key"))

if findKey in data:
    print(findKey," found in data")