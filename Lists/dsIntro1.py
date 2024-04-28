numStudents=5
studentName = []
rollNo = []
engMarks = []
mathMarks = []
sciMarks = []

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
