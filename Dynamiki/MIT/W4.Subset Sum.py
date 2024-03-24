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