salaryComp = {"basicSal":0.35,\
     "hra":0.175,\
     "lta":0.029166667,\
     "cityAllowance":0.428998333,\
     "gratuity":0.016835
 }

companyRec = []
path=r'C:\PythonWork\Data\empRecord.csv'
def printEmpDetails(empRec):
    monthlySal = empRec[5]/12
    print("ID: ", empRec[0], " NAME: ", empRec[1] + " " + empRec[2])
    print("TOTAL YEARLY SALARY: ", empRec[5])
    print("TOTAL MONTHLY SALARY: ", monthlySal, " --- split is as given below:: ")
    print("1 BASIC: ", monthlySal * salaryComp["basicSal"])
    print("2 HRA: ", monthlySal * salaryComp["hra"])
    print("3 LTA: ", monthlySal * salaryComp["lta"])
    print("4 CITY ALLOWANCE: ", (sal / 12) * salaryComp["cityAllowance"])
    print("5 GRATUITY: ", (sal / 12) * salaryComp["gratuity"])


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
    empRec = [id,fName,lName,age,ht,sal,managerId]
    companyRec.append(empRec)

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
    for eRec in companyRec:
        #print(eRec[0],"::::::",eId)
        if(eRec[0]==eId):
            printEmpDetails(eRec)
            flag=1
    if(flag==0):
        print("EMPLOYEE NOT FOUND")

"""
    



    #if(sal > 1100000):
     #   print(line,end="")
    
"""