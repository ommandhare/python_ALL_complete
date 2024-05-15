a=("1","3","4")
b=("1","2","4")


a=set(a)
b=set(b)

inter=a.intersection(b)
print(inter)


union=a.union(b)
print(union)



jaccard=len(inter)/len(union)

print(jaccard)