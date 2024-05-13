# findall function finds all occurrance in string

import re

str="This is spain and its main "

pattern="ain"

result=re.findall(pattern,str)

print(result)

print(f" {pattern}  occurred {len(result)} times in string")