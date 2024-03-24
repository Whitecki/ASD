def simplified_blackjack(T: 'tablica przechowywująca kolejne karty'):
    n = len(T)
    dp = [-1 for _ in range(n)]
    dp[0], dp[n - 1] = 0, 0  # Base case

    for i in range(3, n):  # topological order
        if dp[i - 5] != -1:  # jeśli od ostaniego wzięcia karty odkryte zostały kolejne 5
            win_5 = 0
            a = (T[i - 4] + T[i - 3] + T[i])
            b = (T[i - 2] + T[i - 1])
            if 22 > (T[i - 4] + T[i - 3] + T[i]) > (T[i - 2] + T[i - 1]):
                win_5 = 1
            dp[i] = max(dp[i - 5] + win_5, dp[i])
        if dp[i - 4] != -1:  # jeśli od ostaniego wzięcia karty odkryte zostały kolejne cztery
            win_4 = 0
            if (T[i - 3] + T[i - 2]) > (T[i - 1] + T[i]):
                win_4 = 1
            dp[i] = max(dp[i - 4] + win_4, dp[i])
    result = 0
    for i in range(n - 1, n - 1 - 6, -1):
        result = max(result, dp[i])
    return result


T = [7, 7, 1, 1, 1, 7, 7, 1, 1, 7, 7, 1, 1, 7, 7, 1, 1]
print(simplified_blackjack(T))
