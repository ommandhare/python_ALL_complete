class employee:
    def __init__(self,id,firstName,lastName,age,height,sal,managerId):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.age  = age
        self.height = height
        self.salary = sal
        self.mId = managerId

    def print_emp(self):
        print("EMPLOYEE DETAILS: ")
        print("EMP ID: ",self.id)
        print("EMP NAME: ",self.firstName + " "+ self.lastName)
        print("EMP ATTRIBS --> ", self.age,",",self.height)
        print("EMP SALARY =====>> ",self.salary)
path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\OOP\empRecord.csv"
count=0
empList = []
empObjList = []
for line in open(path):
    if(count==0):
        count +=1
        continue
    print(line,end="")
    id,firstName,lastName,age,height,sal,managerId = line.strip().split(",")
    id = int(id)
    age = int(age)
    height = float(height)
    sal = float(sal)
    managerId = int(managerId)
    empRecord = [id,firstName,lastName,age,height,sal,managerId]
    empList.append(empRecord)
    tempEmp = employee(id,firstName,lastName,age,height,sal,managerId)
    empObjList.append(tempEmp)
print("PRINTING LIST OF LISTS - LIST OF RECORDS")
print(empList)
print("PRINTING LIST OF OBJECTS ----- ")
print(empObjList)
print("*****************************")
for emp in empObjList:
    print(emp)
    emp.print_emp()
### primitive data types
### number, character, floating point number

## derived data types or custom datatypes
##
## 100 - pani purya
## 4 - chincheche pani
## 1/2 kilo - shev
## 1 kilo - farasan
## 1 kilo - batate
## 1 kilo - vatane

### we sell pani puri combo one packet serves 4 ppl
## combo chi 3 pakita dya

## think same for employee record
## id, firstName, lastName,age,height, sal
## give me one employee
"""
class employee {
    int id;
    string fName;
    string lName;
    int age;
    float height;
    float sal;
    int managerId;
}
empTemp = new emp()
"""


emp = employee(111,"Anurag","Devare",34,6.5,100000,2)
#print(emp.id, emp.firstName, emp.salary)



