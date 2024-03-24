def Ten_kupon_to_pewniaczek(S):
    #dp(k,y) - jakie jest prawdopodobieństwo wypradnięcia suma y po k rzutach
    dp = [[0 for _ in range(S+1)] for _ in range(S+1)]
    #Base case: po pierwszym rzucie może wypaść 6 liczb
    # dp[1][1],dp[1][2],dp[1][3],dp[1][4],dp[1][5],dp[1][6] = 1,1,1,1,1,1
    for i in range(1,min(S,7)):
        dp[1][i] = 1
    mniej_niz_S = 0
    wypadlo_S = 0
    for i in range(2,S+1):
        for j in range(i,S+1):
            for k in [-1,-2,-3,-4,-5,-6]:
                if j + k > -1:
                    dp[i][j] += dp[i-1][j+k]*1/6
            if j == S:
                wypadlo_S += dp[i][j]
            else:
                mniej_niz_S += dp[i][j]

    return wypadlo_S / (mniej_niz_S + wypadlo_S)

print(Ten_kupon_to_pewniaczek(120))