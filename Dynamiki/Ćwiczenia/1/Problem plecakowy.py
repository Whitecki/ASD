def pleack(W:'Wartość i-tego przedmiotu',P:'pojemność i-tego przedmiotu',max_P:'pojemność plecaka'):
    n = len(W)
    dp = [[0 for _ in range(max_P+1)] for _ in range(n+1)]
    for j in range(max_P + 1): #Base
        if P[0] < j:
            dp[0][j] = 0
        else:
            dp[0][j] = W[0]

    for i_ty in range(1,n + 1): # topological order
        for waga in range(max_P + 1):
            if waga >= P[i_ty]:#jeżeli pojemność nie wyjebie
                dp[i_ty][waga] = dp[i_ty-1][waga - P[i_ty]] + W[i_ty]
            dp[i_ty][waga] = max(dp[i_ty][waga], dp[i_ty - 1][waga])

    return dp[n][max_P]