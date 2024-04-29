
w1="goa"

w2="yuortgyya"
list=[]

for i in w1:
    # print(i)
    for j in w2:
        if i == j:
            print(i,"==",w2)
            list.append([i,w2])
print(list)