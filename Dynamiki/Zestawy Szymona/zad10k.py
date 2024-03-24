from zad10ktesty import runtests
from math import floor, inf
def dywany ( N ):

    dp = [[i if j == 0 else 0 if i == 0 else inf for j in range(floor(N**.5))] for i in range(N+1)]
    p = [[[] for _ in range(floor(N**.5))] for _ in range(N+1)]
    for i in range(N+1):
        p[i][0] = [1 for _ in range(i)]
    for w in range(1, floor(N ** .5)):
        for i in range(1,N+1):
            dp[i][w] = dp[i][w-1]
            p[i][w] = p[i][w-1]
            if i - (w+1)**2 > -1:
                dp[i][w] = dp[i - (w+1)**2][w] + 1
                p[i][w] = p[i-(w+1)**2][w]
                p[i][w].append(w+1)
    return p[N][floor(N**.5) - 1]


runtests( dywany )

