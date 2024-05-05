def getInterSection(lst1,lst2):
    interSection=[]
    for i1 in lst1:
        for i2 in lst2:
            if i1 == i2:
              interSection.append(i1)
    return interSection

a=[2,4,5,7,9,3,77]
b=[25,9,78,3,5,10,2]


interSection=getInterSection(a,b)
print(interSection)
