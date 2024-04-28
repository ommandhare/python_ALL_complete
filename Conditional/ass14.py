"""
ask user to enter number if number is in 1s then print one, if number is in 10s then print ten if number is in 100s then print hundred if number is in 1000 print thousand. (try to implement this using if-elif-else

"""


num=input("enter the number: ")
num=int(num)
if(1<=num<10):
    print("1s number")
elif(11<=num<100):
   print("10's number")
elif(100<=num<1000):
   print("100's number")
elif(1000<=num<100000):
   print("1000's number")
else:
    print("too much number")

