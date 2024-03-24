from math import inf
def nadal_nwm_czm_poprzednie_nie_dziala(C,S):
    n = len(C)
    sum_C = [C[i] for i in range(n)]
    dp = [inf for _ in range(n)]
    DP = [inf for _ in range(n)]
    dp[0], DP[0] = 0,0
    for i in range(1,n):
        sum_C[i] = sum_C[i-1] + sum_C[i]
        for j in range(0,i):
            DP[i] = min(DP[j] + S[j][i] + sum_C[i-1] - sum_C[j], DP[i])
            dp[i] = min(dp[i],DP[i],dp[j] + sum_C[i] - sum_C[j])
    return dp[n-1]

S = [[6 for _ in range(5)] for _ in range(5)]
P = [1,9,2,4,7]
print(nadal_nwm_czm_poprzednie_nie_dziala(P,S))