from math import inf
def hop_hop(food:"jedzenie"): #O(n^3)
    n = len(food)
    dp = [[inf for _ in range(n)] for _ in range(n)] # minimalna ilość skosów, by dotrzeć do i-tego pola, majac j-energii
    for k in range(food[0]+1):
        dp[0][k] = 0
    for i in range(n):
        for _i in range(i-1,-1,-1):
            for _j in range(n-1,-1,-1):
                if i - _i <= _j and dp[_i][_j] != inf:
                    dp[i][min(food[i] + _j -(i - _i),n-1)] = min(dp[i][min(food[i] + _j - _i,n-1)],dp[_i][_j] + 1)

    result = inf
    for k in range(n):
        result = min(result,dp[n-1][k])

    return result

A = [2, 2, 1, 0, 0, 0]
print(hop_hop(A))

A = [2, 3, 1, 1, 2, 0]
print(hop_hop(A))