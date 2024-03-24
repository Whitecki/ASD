def jebane_n_do_4(A,B,C):
    n = len(A)
    dp = [[[[False for kj in range(n)] for ki in range(n)] for j in range(n)] for i in range(n)]
    dp[0][0][0][0] = True
    for i in range(n):
        for j in range(n):
            for ki in range(n):
                for kj in range(n-ki):
                    if A[i] == C[ki+kj] and ki > 0 and i > 0:
                        dp[i][j][ki][kj] = dp[i][j][ki][kj] or dp[i-1][j][ki-1][kj]
                    if B[i] == C[ki+kj] and j > 0 and kj > 0:
                        dp[i][j][ki][kj] = dp[i][j][ki][kj] or dp[i][j-1][ki][kj-1]
                    if 0 < i < n:
                        dp[i][j][ki][kj] = dp[i][j][ki][kj] or dp[i-1][j][ki][kj]
                    if 0 < j < n:
                        dp[i][j][ki][kj] = dp[i][j][ki][kj] or dp[i][j-1][ki][kj]
    return dp[n-1][n-1][n//2 - 1][n//2 - 1]

A,B,C = "AATT", "CCGG", "AGTC"
print(jebane_n_do_4(A,B,C))