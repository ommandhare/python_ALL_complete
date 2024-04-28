numStudents=5
studentList = []

# range(5) ==> [0,1,2,3,4]
for num in range(numStudents):
    recordList = []
    print("*****************************")
    print("ENTER EXAM DETAILS FOR STUDENT: ",num+1)
    nm = input("Enter Student Name: ")
    recordList.append(nm)
    rN = input("Enter Student roll no: ")
    rN = int(rN)
    recordList.append(rN)
    eng = input("Enter Eng Marks: ")
    eng = int(eng)
    recordList.append(eng)
    math = input("Enter Math Marks: ")
    math = int(math)
    recordList.append(math)
    sci = input("Enter Sci Marks: ")
    sci = int(sci)
    recordList.append(sci)
    studentList.append(recordList)
print("STUDENT LIST: ",studentList)
size = len(studentList)

# ask student to be searched
ch = input("Enter any key to continue/q to exit: ")
while(ch!='q'):
    nm = input("Enter name of the student to be searched: ")
    foundFlag = 0
    for idx in range(size):
        if (nm == studentList[idx][0]):
            print(studentList[idx][0], " FOUND")
            print("ROLL NO: ",studentList[idx][1])
            print("ENG Marks: ",studentList[idx][2])
            print("MATH Marks: ",studentList[idx][3])
            print("SCI Marks: ",studentList[idx][4])
            foundFlag = 1
            break
    if(foundFlag == 0):
        print(nm, " NOT FOUND")
    ch = input("Enter any key to continue/q to exit: ")

print("I HOPE YOU HAD NICE TIME GOOD BYE!!!!!!")
