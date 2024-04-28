from OOP import employee as e
import salaryConfig as s
salaryComp = s.salaryComp
companyRec = []
path=r'C:\PythonWork\Data\empRecord.csv'
def printEmpDetails(empObj):
    monthlySal = round(empObj.salary/12,2)
    print("ID: ", empObj.emp_id, " NAME: ", empObj.name)
    print("TOTAL YEARLY SALARY: ", round(empObj.salary,2))
    print("TOTAL MONTHLY SALARY: ", monthlySal, " --- split is as given below:: ")
    print("1 BASIC: ", round(monthlySal * salaryComp["basicSal"],2))
    print("2 HRA: ", round(monthlySal * salaryComp["hra"],2))
    print("3 LTA: ", round(monthlySal * salaryComp["lta"],2))
    print("4 CITY ALLOWANCE: ", round((sal / 12) * salaryComp["cityAllowance"],2))
    print("5 GRATUITY: ", round((sal / 12) * salaryComp["gratuity"],2))


count=0
for line in open(path):
    if(count==0):
        count +=1
        continue
    #print(line,end="")
    id,fName,lName,age,ht,sal,managerId = line.strip().split(",")
    id = int(id)
    age = int(age)
    ht = float(ht)
    sal = float(sal)
    managerId = int(managerId)
    tempEmp = e.Employee(id,fName+" "+lName,age,ht,sal,managerId)
    #empRec = [id,fName,lName,age,ht,sal,managerId]

    companyRec.append(tempEmp)

print(companyRec)
### write a program to find employee and compute his/her
### salary component details

while(1):
    ch = input("Enter any key/q to exit: ")
    if(ch=="q"):
        break
    eId = input("Enter Emp Id to be searched: ")
    eId = int(eId)
    flag=0
    for eObj in companyRec:
        #print(eRec[0],"::::::",eId)
        if(eObj.emp_id==eId):
            #print("EMPLOYEE FOUND: ")
            #print(eObj.name)
            #eObj.print_employee()
            printEmpDetails(eObj)
            flag=1
    if(flag==0):
        print("EMPLOYEE NOT FOUND")


    



    #if(sal > 1100000):
     #   print(line,end="")
    
