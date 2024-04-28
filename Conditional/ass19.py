"""
get marks for a student and print grade (if < 30, fail, <50 third class, <60 second class, <70 first class, >=70 distinction, =100 then gold medal

"""

mark=float(input("enter the marks/percentage: "))

if(mark<30):
    print("fail")
elif(mark<50):
    print("third class")
elif(mark<60):
    print("second class")
elif(mark<70):
    print("first class")
elif(mark>=70 and mark<99):
    print("distinction")
elif(mark==100):
    print("GOLD")
else:
    print("invalid marks")
