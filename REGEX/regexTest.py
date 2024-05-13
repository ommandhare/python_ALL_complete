import re

str=("my name iss oom ismy friend is hrushi saish  welcome  come on ")

pattern="om?"
result=re.findall(pattern,str)
print(result)

pattern="ism+"
result=re.findall(pattern,str)
print(result)

# print(f"--{pattern}-- occured {len(result)} times in string")