from zad9ktesty import runtests
from math import inf

def prom(P, g, d):
    n = len(P)
    dp = [[[1 if i == 0 and ((P[i] == lg and ld == 0) or (P[i] == ld and lg == 0)) else 0 for lg in range(g+1)] for ld in range(d+1)] for i in range(n)]
    for i in range(1,n):
        flag = False
        for ld in range(d):
            for lg in range(g):
                #daje na dolny
                if ld +P[i] < d+1 and dp[i-1][ld][lg]:
                    dp[i][ld+P[i]][lg] = 1
                    flag = True
                    #daje na górny
                if lg + P[i] < g+1 and dp[i-1][ld][lg]:
                    dp[i][ld][lg + P[i]] = 1
                    flag = True
        if not flag:
            return [1,i-1]
    return [1,n+1]

runtests ( prom )