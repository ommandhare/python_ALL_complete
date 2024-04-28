a=[2,4,5,6,8,9,5,9]
combo={}
pairsList=[]
# for i in range(0,len(a)-1):
#     pairsList=[]
#   for j in range(i+1,len(a)):
#     print(a[i],a[j])
#     pairsList=[a[i],a[j]]
#     if a[i] not in pairsList:
#         combo[a[i]]=pairsList
#     else:
#         combo[a[i]].append(a[j])


for i in a:
    pairsList=[]
    for j in a:
        pairsList.append([i,j])
    combo[i]=pairsList

print(combo)
