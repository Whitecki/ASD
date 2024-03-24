def niby_trudniejsze_ale_w_sumie_latwe_kregle(T):
    n = len(T)

    # maxi(i,j) - maksymalne zbicie wszystkich kręgli pomiędzy i oraz j włącznie
    maxi = [[0 if i != j and i + 1 != j else T[i] if i == j else max(T[i],T[j],T[i]*T[j]) for j in range(n)] for i in range(n)]
    for length in range(2,n):
        for start in range(n-length):
            for k in range(start,start+length):
                maxi[start][start+length] = max(maxi[start][k]+maxi[k+1][start+length],T[start]*T[start+length]+maxi[start+1][start+length-1],maxi[start][start+length])

    #niepotrzebne
    # dp = [0 for _ in range(n)]
    # dp[0],dp[1] = max(T[0],0), max(T[0],T[1],0,T[0]*T[1])
    # for i in range(2,n):
    #     dp[i] = max(dp[i-1],dp[i-1]+T[i],dp[i-2]+T[i-1]*T[i])
    #     for k in range(1,i):
    #         if i-1 >= k + 1:
    #             dp[i] = max(dp[i],dp[k-1] + T[k]*T[i] + maxi[k+1][i-1])
    return maxi[0][n-1]
T = [-2,7,5,5,-5,-5,7,-2]
print(niby_trudniejsze_ale_w_sumie_latwe_kregle(T))