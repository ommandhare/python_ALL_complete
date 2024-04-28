class Student:
    def __init__(self,roll,name,std,age):
        roll=int(roll)
        std=int(std)
        age=int(age)

    def printstudent():
        stdRec=[roll,name,std,age]
        print(stdRec)


path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\OOP\student"

studentList=[]
for line in open(path):
    roll, name, std, age=line.strip().split(",")
    studentObject=Student(roll, name, std, age)
    # print(Student.printstudent())
    studentList.append(line)



for i in studentList:
 print(i)
