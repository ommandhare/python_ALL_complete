
categorPath = r"C:\Users\om\PycharmProjects\python_All\RADAR\category.csv"
descPath =r"C:\Users\om\PycharmProjects\python_All\RADAR\KIRAN\cleandDesc.csv"

descList = []
with open(descPath) as fp:
    for line in fp:
        descList.append(line.strip())

with open(categorPath) as fp:
    idx = 0
    for line in fp:
        tmp=''
        for word in line.strip('" ').split(','):
            tmp+=word+" "
        descList[idx] = descList[idx]+" "+tmp
        idx+=1

with open(r'C:\Users\om\PycharmProjects\python_All\RADAR\KIRAN\cleanData.csv','w') as fp:
    cnt = 0
    for line in descList:
        cnt+=1
        fp.write(line)
    print(cnt)