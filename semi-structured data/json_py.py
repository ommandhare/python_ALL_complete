import json

def analyzeDict(testDict):
    count = 0
    countDict = 0
    for k, v in testDict.items():
        count += 1
        if (type(v) == dict):
            countDict += 1
            print("VALUE IS A DICTIONARY")
        else:
            print("NORMAL VALUE: ", v)
    print("NUMBER OF KEYS IN THIS DICT: ", count)
    print("NUMBER OF KEYS WHERE VALUE IS DICT: ", countDict)
    print("NUMBER OF NORMAL VALUES IN DICT: ", count - countDict)


def dict_recursion(value_dict,level):
    #print("ENDERTED IN DICT RECURSSION>>>>>>> level ", level)
    #print_dict(value_dict)
    next_level= level + 1
    for k, v in value_dict.items():
        if(type(v) is dict):
            print("KEY FOR DICTIONARY: ", k)
            print("DICT FOUND LEVEL OF THIS KEY ",level)
            dict_recursion(v,next_level)
        else:
            print("KEY IS NOT A DICT: ",k, " VALUE IS: ",v)


def print_dict(my_dict):
   for k,v in my_dict.items():
     print("KEY TYPE: ",type(k), " KEY: ", k)
     print("VALUE TYPE: ", type(v), " VALUE: ",v)


#print("KEY: ", "languages", "VALUE: ", person_dict["languages"])
#print("KEY: ", "languages", "1st VALUE in list: ", person_dict["languages"][1])

### read json file and load it as a dictionary
path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\json2.json"
with open(path) as f:
   data = json.load(f)

print("TYPE OF DATA: ",type(data))
print("##############################################################")
#print(data)
#print(data["quiz"]["sport"]["q1"]["answer"])

for k,v in data.items():
   print("***********************")
   print("KEY TYPE: ",type(k), " KEY: ", k)
   print("VALUE TYPE: ",type(v), "VALUE: ",v)
   print("***************************")
   #sport_dict = v['sport']
   #maths_dict = v['maths']
   #print_dict(sport_dict)
   #print_dict(maths_dict)
   #print("VALUE TYPE: ", type(v), " VALUE: ",v)
#print("STARTING RECURSSION FOR JSON OBJECT")
#dict_recursion(data,0)
print("BEFORE ANALYZE DICT FUNCTION")
analyzeDict(data)
print("AFTER ANALYZE DICT FUNCTION")

def browseDictRecurssion(dataDict):
    for k,v in dataDict.items():
        if(type(v)==dict):
            browseDictRecurssion(v)
        else:
            print("KEY: ",k, " VALUE: ",v)

