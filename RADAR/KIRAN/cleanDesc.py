import re
path = r'C:\Users\om\PycharmProjects\python_All\RADAR\internet_des.csv'
cnt  = 0

file = []
with open(path) as f:
    for line in f:
        tmp=""
        for word in line.strip().split(','):
            tmp +=word+" "
        tmp1 =""
        for word in tmp.strip('" ').split('/'):
            tmp1+=word+" "
        row = tmp1.split()
        file.append(row)

for row in file:
    for idx in range(len(row)):
        if(re.match(r"\d",row[idx])):
            spl:list[str] = re.findall(r'[a-zA-Z]+|\d+|\W+',row[idx])
            row[idx] = spl[0]
            for j in range(1,len(spl)):
                row.insert(idx+j,spl[j])

with open(r'C:\Users\om\PycharmProjects\python_All\RADAR\KIRAN\cleandDesc.csv','w') as fp:
    for row in file:
        line =''
        for word in row:
            line+=word+" "
        fp.write(line+"\n")

