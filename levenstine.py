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
                print("----------------------",dp[i][j])
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1


    # Result
    print(dp[m][n])
    return dp[m][n]

# Example usage
s1 = "abcfg"
s2 = "adceg"
i=levenshtein_distance(s1,s2)
print("minimum ditance is ",i)