"""
Write a simple program to get a flag as command line argument.
Read employee file and print first name if flag = 1
and first name and surname if flag = 2

"""

import sys
path=r"C:\Users\om\PycharmProjects\python_All\data\empRecord.csv"
operation_flag = sys.argv[1]
fnameList=[]
fullNameList=[]
cnt=0
for line in open(path):
    if cnt==0:
        cnt+=1
        continue
    else:
        id,fname,lname,age,ht,sal,mId=line.strip().split(",")
        fnameList.append(fname)
        fullNameList.append([fname,lname])



operation_flag=int(operation_flag)
if operation_flag==1:
 print(fnameList)
elif operation_flag==2:
 print(fullNameList)
else:
    print("INVALID CHOICE")