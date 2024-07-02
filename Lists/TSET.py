str1=input("enter:")
str2=input("enter:")

first=[]
for i in str1:
    first.append(i)

second=[]
for j in str2:
    second.append(j)

res=''

for k in first:
    for v in second:
        if k==v:
            if k in v:
               res+=v

print(res)