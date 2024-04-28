import student as s

path =r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\OOP\student_master.txt"
classRecord = []
for line in open(path):
    print(line,end="")
    id, name, ht, wt, age = line.strip().split(",")
    id = int(id) # type assert
    ht = float(ht)
    wt = float(wt)
    age = int(age)
    tempStudent = s.Student(id,name,ht,wt,age)
    classRecord.append(tempStudent)
    print("OBJECT CREATED AT: ",tempStudent)
    print("AGE OF THE CURRENT OBJ: ",tempStudent.stdAge)

print(classRecord)
# write a program to find avg height of the students
size = len(classRecord)
totalHt = 0.0
for stdRec in classRecord:
    totalHt = totalHt + stdRec.stdHt
avgHt = totalHt/size
print("AVERAGE HEIGHT: ",avgHt)

# write a program to print records of only those students
# who's height is more than avg height

for stdRec in classRecord:
    if(avgHt < stdRec.stdHt):
        print("HEIGHT of ",stdRec.name," IS MORE THAN AVG")



height=[]
for ht in classRecord:
    ht.stdHt
    print(ht.stdHt)
    height.append(ht.stdHt)

minHt=height[0]
for ht in height:
    if(minHt>ht):
        minHt=ht



maxHt=height[0]
for ht in height:
    if(maxHt<ht):
       maxHt=ht


print("min ht")
print(minHt)
print("max ht")
print(maxHt)