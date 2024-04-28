import json

def browseDictRecurssion(dataDict):
    for k,v in dataDict.items():
        print("KEY: ",k,"==>",end="")
        if(type(v)==dict):
            print("DICT")
            browseDictRecurssion(v)
        else:
            print(" VALUE: ",v)






#print("KEY: ", "languages", "VALUE: ", person_dict["languages"])
#print("KEY: ", "languages", "1st VALUE in list: ", person_dict["languages"][1])

### read json file and load it as a dictionary
path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\json2.json"
with open(path) as f:
   data = json.load(f)

print("TYPE OF DATA: ",type(data))
browseDictRecurssion(data)