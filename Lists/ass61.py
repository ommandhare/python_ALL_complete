"""
findout Longest peak - input: l1:[3,23,25,4,5,8,2,5,6,7,9,11,3,1,0, 22,34]
--- length of largest peak in this problem is 9

"""
def picDistance(a:list):
    peak = []
    valley = []
    acend = False
    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            if not acend:
                valley.append(i)
            acend = True
        else:
            if acend:
                #peak.append(i)
                acend=False
    #print(peak)
    return valley

def longestPic(b:list):
    longest = [0,0]
    for idx in range(len(b)-1):
        if (longest[1]-longest[0])<(b[idx+1]-b[idx]):
            longest=[b[idx],b[idx+1]]
        # print(max(longest))
    return longest

        #print(one)
        # print(two)


a = [3,23,25,4,5,8,2,5,6,7,9,11,3,1,0, 22,34]
print(a)

valley = picDistance(a)
print(valley)
print("longest:::::")
print(longestPic(valley))