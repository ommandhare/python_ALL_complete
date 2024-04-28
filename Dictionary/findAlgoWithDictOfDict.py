import random
"""
## write a program to get student details from user
## student details should contain following:
 1. id
 2. name
 3. eng marks
 4. math marks
 5. sci marks
 6. history marks
 ## entered student details should stored in separate lists 
 ## 6 different lists to store 6 data elements for each student
 
 ### write step 2 where we will get student name from user
 ### find student name in the list
 ### if student name exists in list then display
 ### details of that student else say not found
 
 """
schoolRecord = {}
idx=0
while(1):
    ch = input("Enter any character/q to exit: ")
    if(ch=='q'):
        break
    idx +=1
    id = idx
    nm = input("Enter Student name: ")
    sci = random.randint(10,99)
    math = random.randint(10,99)
    eng = random.randint(10,99)
    history = random.randint(10,99)
    studentRecord = {"ID":id,"SCI":sci,"NAME":nm,"MATH":math,"ENG":eng,"HISTORY":history}
    schoolRecord[nm]=studentRecord
## out of while loop for data entry
print("out of while loop for data entry")
#size=len(schoolRecord)
## while loop for search on student record

while(1):
    ch = input("Enter any character/q to exit: ")
    if(ch=='q'):
        break
    nm = input("Enter student name to be searched: ")
    if(nm in schoolRecord):
        print("STUDENT FOUND: ")
        print("NAME: ",schoolRecord[nm]["NAME"])
        print("ENG: ",schoolRecord[nm]["ENG"])
        print("MATH: ",schoolRecord[nm]["MATH"])
        print("SCI: ",schoolRecord[nm]["SCI"])
        print("HISTORY: ",schoolRecord[nm]["HISTORY"])
    else:
        print("STUDENT ",nm," NOT FOUND")



