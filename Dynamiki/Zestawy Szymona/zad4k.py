from zad4ktesty import runtests
from math import inf

def falisz ( T ):
    #Tutaj proszę wpisać własną implementację
    n = len(T)
    dp = [[inf for _ in range(n)] for _ in range(n)]
    dp[0][0] = 0
    for i in range(1,n):
        dp[i][0] = dp[i-1][0] + T[i][0]
        dp[0][i] = dp[0][i-1] + T[0][i]
    for i in range(1,n):
        for j in range(1,n):
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + T[i][j]
    return dp[n-1][n-1]

runtests ( falisz )
