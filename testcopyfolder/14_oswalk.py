#!/usr/bin/env python

import os
import sys


# target = "G:\Movies"
target= "H:\JAVA"
total_files = 0
total_dirs = 0
total_size=0

for currdir,subdirs,files in os.walk(target):
    total_dirs += 1   # increment number of directories seen
    total_files  += len(files)  # add the number of files in this dir
    total_size += os.path.getsize(target)

print(target,"DIR contains : ",total_dirs,"dirs","and",total_files,"files","size of dir",total_size)
