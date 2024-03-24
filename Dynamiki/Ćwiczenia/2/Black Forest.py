"""zadanie tak porste, że aż szkoda tracić czasu na jego omawianie. Time: O(n)"""

def czarny_las(T):
    n = len(T)
    dp = [0 for _ in range(n)]
    dp[0],dp[1] = T[0], max(T[0],T[1])
    for i in range(2,n):
        dp[i] = max(dp[i-1],dp[i-2] + T[i])
    return dp[n-1]


# T = [1, 8, 3, 4, 5, 1, 2]
# T = [8, 1, 3, 4, 5, 1, 2]
T = [8, 12, 3, 4, 7, 1, 2, 10]
print(czarny_las(T))
