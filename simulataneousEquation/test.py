a=[4,-3,8,5]
b=[]
print(a[0],a[3])
a[3],a[0]=a[0],a[3]
print("Swap")
print(a[0],a[3])
b.append(a[0])
if a[1]>0:
  a[1]=-a[1]
  print(a[1])
else:
    a[1]=abs(a[1])
    print(a[1])
b.append(a[1])

if a[2]>0:
  a[2]=-a[2]
  print(a[2])
else:
    a[2]=abs(a[2])
    print(a[2])
b.append(a[2])
b.append(a[3])

print("INVERSE")
print(b)
