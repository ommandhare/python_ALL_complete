path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\Dictionary\studentMarks.csv"
print("PATH: ",path)
count=0
classRec = []
for line in open(path):
    count +=1
    if(count==1):
        continue
    print(line,end="")
    sId,sName,eng,math,chem,phy,bio = line.strip().split(",")
    stdRec = [int(sId),sName,float(eng),float(math),float(chem),float(phy),float(bio)]
    classRec.append(stdRec)

print(classRec)
### compute percentage marks for each student and append it to stdRecord
for stdRec in classRec:
    print(stdRec)
    # pct = (eng + math + chem + phy + bio)*100/500
    pct = (stdRec[2] + stdRec[3] + stdRec[4] + stdRec[5] + stdRec[6])/5
    stdRec.append(pct)
    if(pct < 40):
        cls = "FAIL"
    elif(pct < 50):
        cls = "THIRD CLASS"
    elif(pct < 60):
        cls = "SECOND CLASS"
    elif(pct < 70):
        cls = "FIRST CLASS"
    else:
        cls = "DISTINCTION"
    stdRec.append(cls)

print(classRec)

pathW = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\Dictionary\studentdResult.csv"
hdrLine = "student_id,name,eng,math,chem,phy,bio,pct,class\n"
fp = open(pathW,"a")
fp.write(hdrLine)
for stdRec in classRec:
    line = str(stdRec[0]) + "," + \
            stdRec[1] + "," + \
            str(stdRec[2]) +"," +  \
            str(stdRec[3]) + "," + \
            str(stdRec[4]) +"," +  \
            str(stdRec[5]) +"," +  \
            str(stdRec[6]) +"," +  \
            str(stdRec[7]) +"," +  \
            stdRec[8] + "\n"
    fp.write(line)

fp.close()