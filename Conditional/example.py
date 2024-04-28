name=input("enter the student name: ")
mark=float(input("enter the marks/percentage: "))

print("name of student: ", name)
print("percentage: ")
if(mark<40):
    print("fail")
elif(mark>=40 and mark<50):
    print("third class")
elif(mark>=50 and mark<60):
    print("second class")
elif(mark>=60 and mark<70):
    print("first class")
elif(mark>=70):
    print("distinction")
else:
    print("invalid marks")

