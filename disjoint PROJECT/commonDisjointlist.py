newList=[]
# def get_1st_common_disjoints(pair):
#     itemList = []
#     resultList=[]
#     print("################")
#     idx=pair.strip().split("_")
#     print(idx)
#     print(len(idx))
#     for j in idx:
#         j=int(j)
#         print(nDict[j])
#         commonList=[]
#         cnt=0
#         for item in nDict[j]:
#            if item in itemList:
#                 commonList.append(item)
#            elif item in commonList:
#                continue
#            else:
#                itemList.append(item)
#
#     # print("common List:::",commonList)
#     return commonList


def get_common_disjoints(pair,idx):
    itemList = []
    resultList=[]
    print("################")
    for j in idx:
        j=int(j)
        print(nDict[j])
        commonList=[]
        for item in nDict[j]:
           if item in itemList:
                commonList.append(item)
           elif item in commonList:
               continue
           else:
               itemList.append(item)
    print("common List:::",commonList)
    get_common_disjoints(pair,commonList)




nDict={ 1: {2, 3, 4, 5},
    2: {3, 4, 6, 7},
    3: {4, 5, 7, 8},
    4: {5, 6, 8, 9},
    5: {6, 3, 7, 4},
    6 :{5, 7, 2, 1},
    7: {3, 2, 4, 9},
    8: {7, 4, 5, 3},
    9: {8, 2, 6, 3}}

pairList=[]
resultDict={}
commonList=[]

pair=''
for key ,value in nDict.items():
    # print(key,value)
    pair=f"{key}"
    for v in value:
        # print(key,v)
        pair+=f"_{v}"
        # print(pair)
        pairList.append(pair)



# for pair in pairList:
#  get_common_disjoints(pair)


print(" common list:::")
for pair in pairList:
 List=[]
 print(pair)
 idx = pair.strip().split("_")
 get_common_disjoints(pair,idx)



