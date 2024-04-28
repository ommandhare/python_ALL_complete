import json
path=r"C:\PythonWork\Data\test\keyValue.json"

def printDictionary(data):
    for k,v in data.items():
        print("---- KEY: ",k," VAL: ",v)

with open(path) as f:
   data = json.load(f)

if(type(data) == list):
    size = len(data)
    print("LIST FOUND")
    for idx in range(size):
        print("idx: ",idx,"val type: ",type(data[idx]))
        if(type(data[idx])==dict):
            printDictionary(data[idx])
elif(type(data)== dict):
    for k,v in data.items():
        print("KEY: ",k, "K TYPE: ",type(k),end="")
        print("V TYPE: ", type(v)," VAL: ", v, )