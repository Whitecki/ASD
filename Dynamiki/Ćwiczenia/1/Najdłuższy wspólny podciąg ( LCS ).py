def LCS(A,B):
    a,b = len(A), len(B)
    dp = [[0 for _ in range(b)] for _ in range(a)]
    dp[0][0] = 0 #base case
    for i in range(1,b):
        if dp[0][i-1]:
            dp[0][i] = dp[0][i-1]
        if B[i] == A[0]:
            dp[0][i] = 1
    for i in range(1,a):
        if dp[i-1][0]:
            dp[i][0] = dp[i-1][0]
        if B[0] == A[i]:
            dp[i][0] = 1

    for i in range(1,a):
        for j in range(1,b):
            if A[i] == B[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[a-1][b-1]

A = "hieroglyphology"
B = "michaelangelo"
print(LCS(A,B))