a="cat"
b="pat"
alen=len(a)
blen=len(b)

if alen<blen:
    reps=blen
else:
    reps=alen

print(f"Highest range {reps}")

cnt=0
i=0

for i in range(alen):
    print(a[0+i])
print("#######################")
for i in range(blen):
    print(b[0+i])

print("########################")

result=0
for i in range(reps):
    if a[0+i]==b[0+i]:
      # print("inside")
      cnt+=1
    else:
         # print("No")
         result+=1



# print(cnt)

print("diffrence between two is : ", result)


