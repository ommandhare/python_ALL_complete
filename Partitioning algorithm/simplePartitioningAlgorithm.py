# read file country data sample
# count number of lines in the file.
# create 10 files where each file contains equal number or lines
# 5th file can have less number of lines.
path = r"C:\PythonWork\Data\countrydata.csv"
count=0
lineList = []
for line in open(path):
    count +=1
    if(count==1):
       continue
    lineList.append(line)

size = count-1
print("NUM OF LINES IN FILE: ",size)
partLines = int(size/9)
rm =size%9
print("PART LINES: ",partLines," REMAINDER: ",rm)

pathCommon = r"C:\PythonWork\Data\countrydata_NUM.csv"

count=0
fileCnt = 1
pathW=pathCommon.replace("NUM",str(fileCnt))
print(pathW)
fp = open(pathW,'a')
for line in lineList:
    count +=1
    if(count>15):
        fp.close()
        count=1
        fileCnt +=1
        pathW=pathCommon.replace("NUM",str(fileCnt))
        fp = open(pathW,'a')
        fp.write(line)
    else:
        fp.write(line)
fp.close()
        


