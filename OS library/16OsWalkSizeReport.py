#!/usr/bin/env python

import os
import sys


target = "G:\Movies"
#target= "H:\JAVA"
total_files = 0
total_dirs = 0
## os.walk(target) ==> (x,[],[])
for curdir,subdirs,files in os.walk(target):
    #print(curdir)
    pathElements = curdir.split("\\")
    level = len(pathElements)
    #print(pathElements," LEN: ",len(pathElements))
    #print(subdirs)
    total_files = total_files + len(files)
print(total_files)

for dir in subdirs:
        dirpath = curdir + "\\"+dir
        size=os.path.getsize(dirpath)
        print("DIR: ",dir," SIZE: ",size)
        break




