"""
Write a generic sorting function and
sort employee data on different criteria just by giving compare function as input to generic sort function
(*** function pointer)

"""
path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\data\empRecord.csv"
fnameList=[]
cnt=0
for line in open(path):
    if cnt==0:
        cnt+=1
        continue
    else:
        id,fname,lname,age,ht,sal,mId=line.strip().split(",")
        fnameList.append(fname)
        # fullNameList.append([fname,lname])



fnameList=sorted(fnameList)



print(fnameList)