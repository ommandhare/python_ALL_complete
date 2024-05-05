# What is exception?
# What is exception handling?

size = 10
for i in range(size):
    a = i
    try:
       b = (a+5)/(a-5)
    except ZeroDivisionError:
        b = 1000

    print(b)
