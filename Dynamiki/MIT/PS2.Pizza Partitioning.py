from math import inf
# co ciekawe w rozwiązaniu zadania zakłada się możliowśc jedzenia kawałków pizzy zgodnie, jak i przeciwko kierunkowi
# obrotu wskazówek zegara, co jest niezgodne z treścią polecenia
def Zjem_wiecej(T:"smaczność kawałku pomiędzy i, i+1"):
    n = len(T)
    val = [T[i] for i in range(n)]
    val = [val[i-1] + T[i] if i != 0 else T[0] for i in range(n)]
    dp = [[[T[i],T[i]] if i == j else [inf,-inf] for i in range(n)] for j in range(n)]

    for dlugosc in range(2,n//2 +1): # ilość kawałków
        for start in range(1,n-1): # zaczynamy kawałek od startu
            for k in range(dlugosc + 1,dlugosc): #
                dp[start][start+dlugosc][1] = max(dp[start][start+dlugosc][1],dp[start][start+k][0] + val[k,start+dlugosc])
                dp[start][start + dlugosc][0] = min(dp[start][start + dlugosc][0], dp[start][start + dlugosc][0])

    return dp[0][n-1][1]


#kiedys skończę
