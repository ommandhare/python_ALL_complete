a=[5, 3, -8, 4]
b=[2,1]
Q=[]

value=a[0]*b[0]
print(value)
Q.append(value)

value=a[1]*b[1]
print(value)
Q.append(value)

value=a[2]*b[0]
print(value)
Q.append(value)

value=a[3]*b[1]
print(value)
Q.append(value)


print(Q)

xy=[]

value=Q[0]+Q[1]
xy.append(value)

value=Q[2]+Q[3]
xy.append(value)

print(xy)
