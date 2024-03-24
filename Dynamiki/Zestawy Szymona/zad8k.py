from zad8ktesty import runtests
from math import inf


def napraw(s, t):
    n, m = len(s), len(t)
    dp = [[inf if (i != 0 and j != 0) else j if j != 0 else i if i != 0 else 0 for j in range(m + 1)] for i in
          range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[n][m]


runtests(napraw)
