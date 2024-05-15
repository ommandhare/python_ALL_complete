a=("1","3","4")
b=("1","2","4")
c=("55","77")


a=set(a)
b=set(b)

dis=a.isdisjoint(c)
print(dis)

dis=a.isdisjoint(b)
print(dis)