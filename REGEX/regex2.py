import re

multi_str = ''' abcd123@gmail.com
23#45.90
a1@gmail.com
someone@gmail.com
123test.gmail.com
test123t@gmail.com
noone23someone@hotmail.com
2345takeleave.ex
'''
###### '\ is escape sequence that means \ tells to ignore meaning of symbol from the tool specific context
print(multi_str)
print("*********")
pattern = r'[a-z]+[0-9]*[a-z]*@[a-z]+\.com'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

print(multi_str)
print("*********")
pattern = r'[0-9]+[a-z]*@[a-z]+\.com'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")

print(multi_str)
print("*********")
pattern = r'[a-z]+[0-9]*[a-z]@[a-z]+\.com'
match = re.findall(pattern, multi_str)
print("\n\nPATTERN: ",pattern,"\nMATCH: ",match)
print("**********************************************")
