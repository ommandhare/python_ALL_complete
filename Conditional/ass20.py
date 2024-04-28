"""
get a character from user and check if the character is number or vovel or conconent

"""

c=input("enter the character: ")


if  c in ['a','e','i','o','u']:
    print("Vowel")
elif c.isdigit():
    print("number")
else:
    print("consonant")
