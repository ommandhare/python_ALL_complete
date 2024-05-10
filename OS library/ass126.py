"""
Write a program to find out duplicate files and move duplicate files
to a separate folder named filesToBeArchived

"""

import shutil
import os
import hashlib
def moveFile(source,destination):
    try:
        shutil.move(source,destination)
        print(f"{source} moved to {destination}")
    except Exception as e:
        print(f"{source} failed to move {destination} \n\tError:{e}")

def duplicateFile(path):
    fileHashSet = set()
    for root,dirList,fileList in os.walk(path):
        for file in fileList:
            filepath=os.path.join(root,file)
            with open(filepath,'rb') as f:
                fileHash = hashlib.sha256(f.read()).hexdigest()
            if fileHash not in fileHashSet:
                fileHashSet.add(fileHash)
            else:
                moveFile(filepath,r"C:\Users\om\PycharmProjects\python_All\duplic" +file)

duplicateFile(r"C:\Users\om\PycharmProjects\python_All\testcopyfolder")

