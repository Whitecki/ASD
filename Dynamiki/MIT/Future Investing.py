def aspartam_gen_mlodosci(T):
    n = len(T)

    dp = [T[i] for i in range(n)]
    idx = [(0,0) for _ in range(n)]
    # dp[1] = T[0]+ T[1]
    # for i in range(2,7):
    #     Maxi = max(T[:2])
    #     maxi = min(T[:2])
    #     if T[i] > Maxi:
    #         Maxi,maxi = T[i],Maxi
    #     elif T[i] > maxi:
    #         maxi = T[i]
    #     dp[i] = maxi + Maxi
    # idx[0],idx[1],idx[2],idx[3],idx[4],idx[5],idx[6],idx[7] = (0,0),(0,1),(0,1),(0,1),(0,1),(1,5),(1,5),(1,5)
    # dp[0],dp[1],dp[2],dp[3],dp[4],dp[5],dp[6],dp[7] = 7,21,21,21,21,31,31,31
    idx[0],idx[1],idx[2],idx[3],idx[4],idx[5],idx[6],idx[7] = (0,0),(0,1),(1,2),(1,2),(1,2),(1,2),(2,6),(2,6)
    dp[0],dp[1],dp[2],dp[3],dp[4],dp[5],dp[6],dp[7] = 3,10,17,17,17,17,21,21
    for i in range(8,n):
        dp[i], idx[i] = dp[i-1], idx[i-1]
        for k in range(1,8):
            a = T[min(idx[i-k])+7:i]
            b = dp[i-k]
            c = T[i]
            if T[min(idx[i-k])+7:i] != [] and abs(max(idx[i-k]) - i) > 6 and dp[i-k] + max(T[min(idx[i-k])+7:i]) + T[i] >= dp[i]:
                dp[i] = dp[i-k] + max(T[min(idx[i-k])+7:i]) + T[i]
                idx[i] = (max(idx[i-k]),i)
            elif abs(min(idx[i-k]) - i) > 6 and dp[i-k] + T[i] >= dp[i]:
                dp[i] = dp[i - k] + T[i]
                idx[i] = (max(idx[i - k]), i)
    return dp[-1]

T = [8,13,2,2,3,18,7,4,14,15]
T = [3,7,10,2,3,1,11,5,10,13]
print(aspartam_gen_mlodosci(T))