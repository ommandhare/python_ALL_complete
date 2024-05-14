path=r"C:\Users\om\PycharmProjects\python_All\disjoint PROJECT\wordSample"

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
    # print(dp[m][n])
    return dp[m][n]





sWord="carrot"
levDict={}
dist=0
per=0
for word in open(path):
    if len(word) < len(sWord):
        dist = levenshtein_distance(sWord, word)
        per=len(word)-dist/len(word)
    elif len(word) == len(sWord):
        dist = levenshtein_distance(sWord, word)
        if dist==0:
            continue
        per=len(word)-dist/len(word)
    print(f"{sWord}:sWord,{word}:word,{dist}:dist,{per}:per")
