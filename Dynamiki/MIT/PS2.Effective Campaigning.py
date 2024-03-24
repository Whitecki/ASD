def polityka(D,Z):
    n = len(D)
    dp = [0 for _ in range(n)]
    dp[0],dp[1],dp[2] = D[0],max(D[0]+Z[1], D[1]+Z[0]), max(D[0]+Z[1]+Z[2], D[1]+Z[0]+Z[2],D[2]+Z[1]+Z[0])
    for i in range(3,n):
        dp[i] = max(dp[i-3] + D[i] + Z[i-1] + Z[i-2], dp[i-1] + Z[i])
    return dp[n-1]

