def zmodyfikowany_pleack(T:'Wartość i-tej liczby',max_P:'szukana wartość'):
    n = len(T)
    dp = [[0 for _ in range(max_P+1)] for _ in range(n+1)]
    for j in range(max_P + 1): #Base
        if T[0] < j:
            dp[0][j] = 0
        else:
            dp[0][j] = T[0]

    for i_ty in range(1,n + 1): # topological order
        for waga in range(max_P + 1):
            if waga >= T[i_ty]: #jeżeli pojemność nie wyjebie
                dp[i_ty][waga] = dp[i_ty-1][waga - T[i_ty]] + T[i_ty]
            dp[i_ty][waga] = max(dp[i_ty][waga], dp[i_ty - 1][waga])

    if dp[n][max_P] == max_P:
        return True
    return False


def sumujemy(T:"tablica liczb",x:"liczba którą mamy wysumować z liczb należących do T"):
    n = len(T)
    dp = [[True if i == 0 else False for i in range(x+1)] for _ in range(n)]
    dp[0][T[0]] = True
    result = False
    for i in range(1,n):
        for j in range(1,x+1):
            if -1<j-T[i]<x+1 and dp[i-1][j-T[i]]:
                dp[i][j] = True
            else:
                dp[i][j] = dp[i][j] or dp[i-1][j]
        result = result or dp[i][x]
    return result

T = [3,0,5,2,7,13,8]
x = 9
print(sumujemy(T,x))

T = [3,0,5,2,7,13,8]
