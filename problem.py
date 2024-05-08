import random
def getcombination(fnameList,lnameList):
    count=0
    for name in nameList:
        for lastName in surnameList:
            count+=1
            fullName = name + "_" + lastName
            print(fullName)
    return count




path1 = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\firstNames.csv"
nameList=[]
count=0
for i in open(path1):
    if(count==0):
        count+1
    sr_no,name,gender=i.strip().split(",")
    # print(name)
    nameList.append(name)
print(nameList)

path2 = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\lastNames.csv"

surnameList=[]

for j in open(path2):
    if (count == 0):
        count + 1
    sr_no, lastName = j.strip().split(",")
    # print(i)
    surnameList.append(lastName)
print(surnameList)

citizenList=[]
for name in nameList:
    for lastName in surnameList:
       fullName=name+"_"+lastName
       print(fullName)
       print("Total ", count, " generated")

