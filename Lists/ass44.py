"""
ask user to enter a string and check if the string is a palindrome

"""

str=input("enter the string")
pal=True
for i in range(len(str)):
  if str[i]!=str[len(str)-i-1]:
      pal=False

if pal:
    print("palindrome")
else:
    print("not palindrome")


