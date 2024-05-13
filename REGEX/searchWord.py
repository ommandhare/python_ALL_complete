import re

str="name is om my"

result=re.search("my",str)

print(result)

if result:
    print("Found in string.")
else:
    print("Not Found.")