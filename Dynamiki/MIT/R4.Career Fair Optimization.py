def jakie_twoje_wady_stara_zakryć_się_ta_metka(C: "fajność i-tych butów", W: "waga i-tych butów",
                                               T: "czas stania w i-tych butach", MaxW: "waga plecaka",
                                               MaxT: "czas na zbieranie swag-u",h:"czas powrotu do domu"):
    n = len(C)
    # dp(i,b,k) - maksymalna ilosć swag-u jaką zgarnie nasz kumpel, mając do dsypozycji plecak o pojemności b, k czasu
    # oraz i pierwszych butów
    dp = [[[0 for k in range(MaxT + 1)] for b in range(MaxW + 1)] for i in range(n + 1)]

    for i in range(1,n+1):
        for b in range(1,MaxW):
            for k in range(1,MaxT):
                if b - W[i-1] > -1 and k - T[i-1] - 1 > -1:
                    dp[i][b][k] = max(dp[i][0][k-T[i-1] - 1],dp[i-1][b-W[i-1]][k-T[i-1]-1],dp[i-1][b][k])
                elif k - T[i-1] - 1 > -1:
                    dp[i][b][k] = max(dp[i][0][k - T[i - 1] - 1], dp[i - 1][b - W[i - 1]][k - T[i - 1] - 1],
                                      dp[i - 1][b][k])
                else:
                    dp[i][b][k] = dp[i-1][b][k]
                #odkładam wszystko i następne buty wkłądam do pustego plecaka
                if i < n and k-T[i+1-1]-2 - h > -1:
                    dp[i+1][0][k-T[i+1-1]-1] = dp[i][b][k-T[i+1-1]-h - 2]
    return dp[n][MaxW][MaxT]