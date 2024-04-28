"""
Write a program to find out duplicate files and move duplicate files to a separate folder named filesToBeArchived

"""

import os

root_dir = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\reward project"


fileLIST=[]
seenList=[]
duplicateList=[]
for dir,subdir,files in os.walk(root_dir):
    if files in seenList:
        duplicateList.append(files)
    else:
        seenList.append(files)

for files in os.listdir(root_dir):
    print(files)


print(seenList)
print(duplicateList)

