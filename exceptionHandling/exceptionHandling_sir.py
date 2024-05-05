# What is exception?
# What is exception handling?

a = input("Enter a number: ")

a = int(a)

try:
   b = (a+5)/(a-5)
   print("B: ",b)
except ZeroDivisionError:
    print("we are good")

print("FINAL FINAL FINAL")