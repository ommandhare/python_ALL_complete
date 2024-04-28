a=[5,4,6,7]

peaks=[]

for i in a:
        if a[i]<= a[i+1]:
           high=a[i+1]
           print(high)
        else:
            continue
# print(peaks)
