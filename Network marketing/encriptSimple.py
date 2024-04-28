#create one string with required alphabets
# lets say 'a-z'
# calculate length of that string == 26
# for 1 to 26 -- for every number get a random number
# between 1 and 26 and print that pair



import random
path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\Network marketing\pairs.csv"
enStr = "abcdefghicklmnopqrstuvwxyz 1234567890,-;<>=!@#$%^&*(){}[]|`+"
size = len(enStr)
print(size)
pairDict = {}
f = open(path,"a")
for i in range(size):
    n = i+1
    if(n in pairDict):
        continue
    else:
        while(1):
            pr = random.randint(1,60)
            if(pr in pairDict or n==pr):
                continue
            else:
                pairDict[n] = pr
                pairDict[pr] = n
                ln = str(n) + "," + str(pr) + "\n"
                f.write(ln)
                break
f.close()