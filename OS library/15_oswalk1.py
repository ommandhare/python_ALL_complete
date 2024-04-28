#!/usr/bin/env python

# find files whose size is greater than 100K bytes
import sys
import os
'''
if sys.platform == 'win32':
    target = 'C:/Windows'
else:
    target = '/Users/mandarkale'
'''
target = "D:\PythonWork"
out_file = "D:\PythonWork\dir_files16JUNE11.csv"

#regular expressions
# add current directory to dict
# keep cumulative file size and no of files as value in dict
#key = dir, value = [no of file, size]

f = open(out_file,"a")
for currdir,subdirs,files in os.walk(target):
    for file in files:
        print(file)
        fullpath = os.path.join(currdir,file)
        fsize = os.path.getsize(fullpath)
        line = currdir + "," + str(fsize)+","+ fullpath + "\n"
        f.write(line)
        print(fullpath)
        
f.close()


#[[c:,[sub1,sub2,sub3],[file1,file2,file3]],[sub1,[sub11,sub12],[sub1file1,sub1file2]],]
        
'''
        try:
            fsize = os.path.getsize(fullpath)
        except OSError as e:
            continue
        if fsize > 100000:
            print(fullpath)
'''
