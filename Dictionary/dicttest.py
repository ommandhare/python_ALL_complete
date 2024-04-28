newDict={}
with open(r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\Dictionary\usrpwd.txt") as file:
    for line in file:
        usr,pwd=line.strip().split(":")
        newDict[usr]=pwd

print(newDict)


name = input("Enter the username :")

if name in newDict:
    print("VALID NAME")
    password = input("valid name Enter the password :")
    if newDict[name]==password:
        print("Valid password ")
    else:
        print("invalid password")
else:
    print("invalid username")

