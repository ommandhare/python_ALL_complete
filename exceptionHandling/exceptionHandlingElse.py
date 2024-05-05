# What is exception?
# What is exception handling?

size = 10
for i in range(size):
    a = i
    try:
       b = (a+5)/(a-5)
    except ZeroDivisionError:
        b=1000
        print("due to exception i am setting value of b=",1000)
        print("Division by zero error occured for a=",a)
    else:
        print(b)
    finally:
        print("THIS LINE IS ALWAYS EXECUTED: ",b)
