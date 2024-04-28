##
import networkMember as m

def addNodeToLevelDict(nd, levelDict, l):
    if (l in levelDict):
        nodeList = levelDict[l]
        nodeList.append(nd)
        levelDict[l] = nodeList
    else:
        nodeList = []
        nodeList.append(nd)
        levelDict[l] = nodeList


def browseTreeAddConfLevelDict(node, memberDict, childDict, levelDict, lvl):
    addNodeToLevelDict(node, levelDict, lvl)
    if (node.id in childDict):
        childList = childDict[node.id]
        for child in childList:
            browseTreeAddConfLevelDict(child, memberDict, childDict, levelDict, lvl + 1)


path=r"C:\Users\om\PycharmProjects\python_All\Network marketing\networkMarketing.csv"
cnt=0
memberDict ={} # member id as key and memeber obj as value
childDict = {} # member id as key and list of child obj as value
rootNode = ""
levelDict = {}

for line in open(path):
    if(cnt==0):
        cnt +=1
        continue
    #print(line,end="")
    id,fName,lName,regStore,regDate,parentId = line.strip().split(",")
    tempMember = m.Member(int(id),fName,lName,int(regStore),regDate,int(parentId))
    memberDict[int(id)] = tempMember #this step saves member info and parent info
    if(tempMember.parentId == -1000):
        rootNode = tempMember
    if(tempMember.parentId in childDict):
        childList = childDict[tempMember.parentId]
        childList.append(tempMember)
        childDict[tempMember.parentId] = childList
    else:
        childList = []
        childList.append(tempMember)
        childDict[tempMember.parentId] = childList

## tree is built
print(rootNode.id)
childList = childDict[rootNode.id]
print(childList)
browseTreeAddConfLevelDict(rootNode,memberDict,childDict,levelDict,0)
for l,lst in levelDict.items():
    print("LEVEL: ",l)
    print("LIST OF NODES: ",lst)