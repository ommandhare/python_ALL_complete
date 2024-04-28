numStudents=5
studentName = []
rollNo = []
engMarks = []
mathMarks = []
sciMarks = []
# range(5) ==> [0,1,2,3,4]
for num in range(numStudents):
    print("*****************************")
    print("ENTER EXAM DETAILS FOR STUDENT: ",num+1)
    nm = input("Enter Student Name: ")
    studentName.append(nm)
    rN = input("Enter Student roll no: ")
    rN = int(rN)
    rollNo.append(rN)
    eng = input("Enter Eng Marks: ")
    eng = int(eng)
    engMarks.append(eng)
    math = input("Enter Math Marks: ")
    math = int(math)
    mathMarks.append(math)
    sci = input("Enter Sci Marks: ")
    sci = int(sci)
    sciMarks.append(sci)

print("STUDENT NAME: ",studentName)
print("ROLL NO: ", rollNo)
print("ENG MARKS: ",engMarks)
print("MATH MARKS: ",mathMarks)
print("SCI MARKS: ",sciMarks)

# ask student to be searched
ch = '2'
while(ch!='q'):
    ch = input("Enter any key to continue/q to exit: ")
    if(ch=='q'):
        continue
    nm = input("Enter name of the student to be searched: ")
    foundFlag = 0
    for name in studentName:
        if(nm == name):
            print(nm," FOUND")
            foundFlag = 1
            break
    if(foundFlag==0):
        print(nm," NOT FOUND")

print("I HOPE YOU HAD NICE TIME GOOD BYE!!!!!!")
