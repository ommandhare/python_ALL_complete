# Find longest pic in the list i.e. mountain which is longest
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


a = [5, 6, 7, 7, 5, 2, 4, 3, 1, 7, 6, 8, 4, 3, 2]
print(a)

valley = picDistance(a)
print(valley)
print("longest:::::")
print(longestPic(valley))
