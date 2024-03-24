def gruby_bedziesz(T,S,C):
    n = len(T)
    t = [(0,0,0) for _ in range(n+1)]
    for i in range(1,n+1):
        t[i] = T[i-1]
    dp = [[[0 for _ in range(S+1)] for _ in range(C+1)] for _ in range(n+1)]
    for i in range(t[1][1],C+1):
        dp[1][i][t[1][2]] = t[1][0]
    for s in range(S + 1):
        for i in range(2,n+1):
            for c in range(C+1):
                dp[i][c][s] = dp[i - 1][c][s]
                if c - t[i][1] > -1: #jeśli jest wystarczająco kalorii
                    if s > 0: # czy mogę wziąć słodki
                        if dp[i - 1][c - t[i][1]][s - t[i][2]] != 0:
                            dp[i][c][s] = max(dp[i][c][s], dp[i - 1][c - t[i][1]][s - t[i][2]] + t[i][0])
                    else:
                        if not t[i][2]: # maksymalna słodkość obiadu bez cukru nie może się skłądać z dania z cukrem
                            dp[i][c][s] = max(dp[i][c][s], dp[i - 1][c - t[i][1]][s - t[i][2]] + t[i][0])
    return dp[-1][-1][-1]

T = [(5,10,1), (12,21,0), (28,18,1), (37,15,0), (15,2,1), (21,17,1)]
print(gruby_bedziesz(T,3,30))