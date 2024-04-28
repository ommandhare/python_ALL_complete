import json
#path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\recursion\keyValue.json"
#"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\recursion\listOfList.json"
#"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\recursion\dictOfDict.json"
path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\recursion\dictOfDictContainingLists.json"

def browseDictionary(data):
    for k,v in data.items():
        if(type(v)==list):
            print("VALUE FOR K: ",k, " is a list---- calling list recurssion")
            browseList(v)
        elif(type(v)==dict):
            print("VALUE FOR K: ",k," is a dict-----")
            browseDictionary(v)
        else:
            print("VALUE: ",v)


def browseList(data):
    size = len(data)
    for idx in range(size):
        if(type(data[idx])==list):
            print("LIST FOUND -- calling recurssion")
            browseList(data[idx])
        elif(type(data[idx])==dict):
            print("Dict found -- calling dict recurssion")
            browseDictionary(data[idx])
        else:
            print("VALUE FOUND: ",data[idx])

with open(path) as f:
   data = json.load(f)

print("welcome to browse")

if(type(data)==list):
    browseList(data)
elif(type(data)==dict):
    browseDictionary(data)
else:
    print(data)

