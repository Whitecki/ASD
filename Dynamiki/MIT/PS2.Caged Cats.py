from math import inf


def kotki(Tigers: "[ age,size] ", Cages: " [ distance,capacity ] "):
    sorted(Tigers, key=lambda x: x[0])
    sorted(Cages, key=lambda x: x[0])
    n = len(Tigers)
    dp = [[0 if (i == 0 and j > 0 and Tigers[i][1] >= Cages[j][1]) else Tigers[i][1] - Cages[j][1] if
    (i == 0 and j > 0 and Tigers[i][1] < Cages[j][1]) else inf for i in range(n ** 2 + 1)] for j in
          range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, n ** 2 + 1):
            discomfort = 0
            if Tigers[i][1] < Cages[j][1]:
                discomfort = Tigers[i][1] - Cages[j][1]
            dp[i][j] = min(dp[i - 1][j - 1] + discomfort, dp[i][j - 1], dp[i][j - 1])
    return dp[n][n**2]
