import random


pairDict={}
for i in range(30):
    n = random.randint(1, 60)
    pr = random.randint(1, 60)
    if(n in pairDict):
        continue
    while(1):
        if (pr in pairDict or n==pr):
            # print("SKIPPED")
            break
        else:
            pairDict[n]=pr
            pairDict[pr]=n
            # print("pair created")


print("PAIR CREATED")
print(pairDict)
for k,v in pairDict.items():

    print(k,v)

