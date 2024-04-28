##
import networkMember as m
path=r"C:\Users\om\PycharmProjects\python_All\Network marketing\networkMarketing.csv"
cnt=0
def getMemberHierarchyMx(mId,mDict,level,maxL):
    mOb = mDict[mId]
    p = mOb.parentId
    if(p == -1000 or level== maxL):
        #printRecurData(level,"-")
        print(mOb.firstName)
        hk = mOb.firstName
        return hk
    else:
        #printRecurData(level,"-")
        print(mOb.firstName,"==>",end="")
        hk = getMemberHierarchyMx(mOb.parentId,mDict,level+1,maxL)
        return hk +"->" + mOb.firstName

def printRecurData(lv,ch):
    for i in range(lv):
        print(ch,end="")

def getMemberHierarchy(mId,mDict,level):
    mOb = mDict[mId]
    p = mOb.parentId
    if(p == -1000):
        #printRecurData(level,"-")
        print(mOb.firstName)
        hk = mOb.firstName
        return hk
    else:
        #printRecurData(level,"-")
        print(mOb.firstName,"==>",end="")
        hk = getMemberHierarchy(mOb.parentId,mDict,level+1)
        return hk +"->" + mOb.firstName
## new program --
# find number of nodes in tree of given node
def countNodes(id,cDict):
    retCnt = 0
    if(id in cDict):
        print("child list found for node: ",id)
        cList = cDict[id]
        cnt=1
        print(cList)
        for child in cList:
            print("CHILD ID: ",child.id)
            cnt += countNodes(child.id, cDict)
            retCnt = cnt
    else:
        print("leaf found: ",id)
        retCnt =  1
    return retCnt
def findLeafNodes(mId,mDict,cDict,lvl):
    if(mId in cDict):
        mObj = mDict[mId]
        for cNode in cDict[mId]:
            cId = cNode.id
            findLeafNodes(cId,mDict,cDict,lvl+1)
    else:
        print("LEAF NODE FOUND:::\nID:",mDict[mId].id,"\tNAME: ",mDict[mId].firstName," AT level: ",lvl)

memberDict ={} # member id as key and memeber obj as value
childDict = {} # member id as key and list of child obj as value
for line in open(path):
    if(cnt==0):
        cnt +=1
        continue
    #print(line,end="")
    id,fName,lName,regStore,regDate,parentId = line.strip().split(",")
    tempMember = m.Member(int(id),fName,lName,int(regStore),regDate,int(parentId))
    memberDict[int(id)] = tempMember #this step saves member info and parent info
    if(tempMember.parentId in childDict):
        childList = childDict[tempMember.parentId]
        childList.append(tempMember)
        childDict[tempMember.parentId] = childList
    else:
        childList = []
        childList.append(tempMember)
        childDict[tempMember.parentId] = childList

print(memberDict)
print(childDict)
## browse member dict
## for every member print all parent hierarchy of that member
for mId,mObj in memberDict.items():
    print(mId," NAME: ",mObj.firstName)

print("PRINGING MEMBER HIERARCHY")
#hierarchy = getMemberHierarchy(1298,memberDict,0)
hierarchy = getMemberHierarchyMx(1298,memberDict,0,5)

print(hierarchy)
"""
m = 1992
findLeafNodes(1992,memberDict,childDict,0)

c = 1298
cnt = countNodes(1992,childDict)
print("NODES UNDER C: ",c," are: ",cnt)

## write a recursion that acceptes memberId, memberDict, level and  maxLvl
## and get member hierarchy till maxLevel
## hierarchy = getMemberHierarchyML(1298,memberDict,0,5)
"""