import json

path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\json2.json"
with open(path) as f:
   data = json.load(f)


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


dict_recursion(data,0)