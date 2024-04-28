"""
read the testDuplicate file and find duplicate lines in file

"""


path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\File Read\duplicate"
lineList=[]
duplicateList=[]
for line in open(path):
    print(line)

for line in open(path):
    line=line.strip().split(",")

    if(line in lineList):
        duplicateList.append(line)
    else:
        lineList.append(line)

print("line List")
print(lineList)
print("duplicate List   ")
print(duplicateList)




