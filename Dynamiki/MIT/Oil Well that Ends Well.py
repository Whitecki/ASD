from math import inf
def PSG(m,a,p,s):
    n = len(a)
    A,P = [0 for _ in range(n+1)], [0 for _ in range(n+1)]
    for i in range(n):
        A[i+1],P[i+1] = a[i], p[i]
    dp = [[-inf if i!=0 and j!= 0 else 0 if i == 0 else -s*i for j in range(n+1)] for i in range(m+1)]
    for j in range(1,n+1):
        for i in range(1,m+1):
            dp[i][j] = max(dp[i-1][j] - s,dp[i][j-1])
            if i - A[j] > -1:
                dp[i][j] = max(dp[i][j],dp[i-A[j]][j-1]+P[j])
    return dp[m][n]

a = [3,7,5,10]
p = [8,10,35,40]
m = 10
s = 5
print(PSG(m,a,p,s))

