from math import inf


def min(T):
    n = len(T)
    #Base
    dp = [[inf if j != 0 else T[i] for j in range(n)] for i in range(n)]
    for dlugosc in range(1,n+1):
        for start in range(n - dlugosc):
            i = start
            j = start + dlugosc
            for kreske_stawiam in range(i,j):
                dp[i][j] = min(dp[i][j],dp[i][kreske_stawiam] + dp[kreske_stawiam+1][j])
    return dp[0][n-1]

A = [5, 2, 7, 1, 6, 3, 8, 4, 2, 7]
k = 3