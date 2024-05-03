"""
Write a generic sorting function and
sort employee data on different criteria
just by giving compare function as input to generic sort function
(*** function pointer)

"""
path=r"C:\Users\om\PycharmProjects\python_All\data\empRecord.csv"
fnameList=[]
lnameList=[]
cnt=0

def compare(value):
    if

for line in open(path):
    if cnt==0:
        cnt+=1
        continue
    else:
        id,fname,lname,age,ht,sal,mId=line.strip().split(",")
        fnameList.append(fname)
        lnameList.append(lname)




fnameList=sorted(fnameList)



print(fnameList)