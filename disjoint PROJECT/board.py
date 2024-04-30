for line in pairList:
    # print(line)
    idx=line.strip().split("_")
    # print(idx)
    for j in idx:
     j=int(j)
     print(nDict[j])




for key ,value in nDict.items():
    # print(key,value)
    pair = f"{key}"
    for v in value:
        # print(key,v)
        pair += f"_{v}"
        V= pair.strip().split("_")
        print("opened")
        print(V)
        for j in V:
          j=int(j)
          print(nDict[j])
