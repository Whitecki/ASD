from zad6ktesty import runtests


# zadanie jest wykonane poprawenie, ale tesy zakłądają że litera A ma idx równy 1.
# u mnie Litera A ma idx  = 0. Stąd

def haslo(S):
    n = len(S)
    # dp[i,boll] -
    # boll == 1 - ile kombinacji T[:i] ma sklejone litery o idx i-1 oraz i - 2
    dp = [[0, 0] for _ in range(n)]
    if int(S[0:2]) < 26:
        dp[1][0], dp[1][1] = 1, 1
    else:
        dp[1][0], dp[1][1] = 1, 0
    for i in range(2, n):
        if S[i - 1] == "1" or (S[i - 1] == "2" and int(S[i]) < 7):
            dp[i][1] += dp[i - 1][0]
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]

    return dp[n - 1][0] + dp[n - 1][1]

# print(haslo("422031421512"))
runtests(haslo)
