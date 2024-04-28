# Write a program to store
# student id, name, age, pct marks
# store all this information for 5 students
# print information of the student with max marks

classRecord = []
while(1):
    ch = input("Enter any key to continue/q to exit: ")
    if(ch=='q'):
        break
    studentRecord = []
    # studentRecord = [10,"Aarya",56,98]
    # classRecord = [[stdRec],[stdRec],[stdrec]]
    id = input("Enter Student Id: ")
    studentRecord.append(int(id))
    name = input("Enter Student Name: ")
    studentRecord.append(name)
    age = input("Enter Student age: ")
    studentRecord.append(int(age))
    pct = input("Enter Student pct: ")
    studentRecord.append(float(pct))
    classRecord.append(studentRecord)

print(classRecord)

## program to find student with max marks
size = len(classRecord)
maxIdx = 0
maxMark = -10
for idx in range(size):
    stdRec = classRecord[idx]
    if(maxMark < stdRec[3]):
        maxMark = stdRec[3]
        maxIdx = idx

print("TOPPER IS: ",classRecord[maxIdx][1]," with percentage of ", classRecord[maxIdx][3])
