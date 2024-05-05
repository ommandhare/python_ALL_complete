a=int(input("Enter the range::::"))
b=0
for i in range(a):
    try:
        b = (a + 5) / (a - 5)
    except ZeroDivisionError:
        print("I IS ZERO.....")
    else:
        print(b)


