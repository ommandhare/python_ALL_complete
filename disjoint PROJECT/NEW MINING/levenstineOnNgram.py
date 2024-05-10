path=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\cleanedData.csv"

def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    # Initialize the matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # Initialization
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    # Filling the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
                # print(dp)
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1


    # Result
    # print(dp[m][n])
    return dp[m][n]




worda=("STRAWBERRY")
worda=worda.upper()
List=[]
n=3

for i in range(len(worda)-n+1):
     ngram=''
     for j in range(n):
         ngram+= worda[i+j]
     List.append(ngram)

print(List)

firstGram=List[0]
secondGram=List[1]
print(firstGram)
print(secondGram)

nDict={}
fList=[]
for line in open(path):
    words=line.strip().split(",")
    # print(words)
    for word in words:
        # print(word)
        if (firstGram in word[:3] and secondGram in word[:6]):
             fList.append(word)


# print(fList)


for i in fList:

    distance=levenshtein_distance(worda,i)
    if distance == 4:
     print(i)
     print(distance)
