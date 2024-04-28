# Write a program to store
# student id, name, age, pct marks
# store all this information for 5 students
# print information of the student with max marks

classRecord = []
# read student data from file
path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\OOP\student_master.txt"
for line in open(path):
    print(line)
    id,name,ht,wt,age = line.strip().split(",")
    studentRecord = []
    studentRecord.append(int(id))
    studentRecord.append(name)
    studentRecord.append(float(ht))
    studentRecord.append(float(wt))
    studentRecord.append(int(age))
    classRecord.append(studentRecord)

print(classRecord)

## program to find student with max ht
size = len(classRecord)
maxIdx = 0
maxAttrib = -1
for idx in range(size):
    stdRec = classRecord[idx]
    if(maxAttrib < stdRec[3]):
        maxAttrib = stdRec[3]
        maxIdx = idx

print("Student with max height is: ",classRecord[maxIdx][1],"with" ,classRecord[maxIdx][3])

