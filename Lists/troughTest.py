a=[5,10,5,7,4,6,7,9,25,2,7,4,7]
n=len(a)
for i in range(n-1):
    if(a[i]<a[i+1]):
        print(a[i])