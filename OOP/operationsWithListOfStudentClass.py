# Write a program to store
# student id, name, age, pct marks
# store all this information for 5 students
# print information of the student with max marks

## lets create a student class
class Student:
    # int stdId;
    # str studentName;
    # float height;
    # float weight;

   def  __init__(self,stdId,name,stdHt,stdWt,stdAge): ### constructor
       self.stdId = stdId
       self.name = name
       self.stdHt = stdHt
       self.stdWt = stdWt
       self.stdAge = stdAge
   def printStudent(self):
       print("\n################# GREAT GREAT GREAT#########################")
       print("STUDENT ID::::",self.stdId)
       print("STUDENT NAME::: ",self.name)
       print("STUDENT HEIGHT::: ",self.stdHt)
       if(self.stdAge > 60):
           print("############## SENIOR #########################")
       print("$##$#$#$#$#  STUDENT AGE::: ", self.stdAge , " @!@!@!@!@!@!!@!")
       print("*****************************************************")

classRecord = []
path =r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\OOP\student_master.txt"
for line in open(path):
    print(line,end="")
    id, name, ht, wt, age = line.strip().split(",")
    id = int(id)
    ht = float(ht)
    wt = float(wt)
    age = int(age)
    tempStudent = Student(id,name,ht,wt,age)
    classRecord.append(tempStudent)
    #tempStudent.printStudent()
    print(tempStudent)

# print("FINAL VALUE IN TEMPSTUDENT: ",tempStudent)

print(classRecord)
maxHt = -1000
maxIdx = -10
size = len(classRecord)
for idx in range(size):
    studentRec = classRecord[idx]
    if(maxHt < studentRec.stdHt):
        maxHt = studentRec.stdHt
        maxIdx = idx

print("STUDENT WITH MAX HEIGHT: ")
classRecord[idx].printStudent()