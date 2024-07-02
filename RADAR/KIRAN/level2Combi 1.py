def dataExt(path):
    file=[]
    with open(path) as fp:
        next(fp)
        for line in fp:
            line = line.strip().split(',')
            file.append(line)
    return file


def comb(lst):
    if len(lst) == 1:
        return lst
    curr = lst[0]
    currList = comb(lst[1:])
    ret =[]
    for i in range(len(currList)):
        if curr == currList[i]:
            continue
        if type(currList[i]) == tuple:
            tmp = [curr]
            for wd in currList[i]:
                tmp.append(wd)
            ret.append(tuple(tmp))
        else:
            ret.append((curr, currList[i]))
    return [curr]+ret+currList

def wordCount(file,wd):
    cnt =0
    for line in file:
        for cwd in line:
            if wd == cwd:
                cnt+=1
    return cnt

def setCount(file,words):
    cnt = 0
    for line in file:
        cmp = set(line)
        flag = True
        for word in words:
            if word not in cmp:
                flag =False
                break
        if flag :
            cnt+=1
    return cnt





def wordFreq(file):
    freq = {}
    for line in file:
        cmb = comb(line)
        for token in cmb:
            if type(token) == str and token not in freq:
                cnt = wordCount(file,token)
                freq[token] = (cnt ,1)
            elif token not in freq:
                cnt = setCount(file,token)
                freq[token] = (cnt,len(token))
    return freq

def store(fq:dict):
    data = []
    for k,v in fq.items():
        data.append((k,v[1],v[0]))
    data = sorted(data ,key=lambda obj:obj[1])
    with open(r'frequency.csv','w') as fp:
        fp.write('Item,Size,Frequency\n')
        for obj in data:
            fp.write(f"{obj[0]},{obj[1]},{obj[2]}\n")



def main():
    dataPath = r'C:\Users\om\PycharmProjects\python_All\RADAR\KIRAN\data2.csv'
    file = dataExt(dataPath)
    print("File read")
    fq = wordFreq(file)
    print("Frequency extracted")
    store(fq)
    print("Done")



if __name__ == '__main__':
    main()