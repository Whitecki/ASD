"""
rozwiązanie O(n^2)
dp[i] - najwyższa wierza, w której znajduje i-ty klocek

rozwiązanie O(nlogn)
oparte o idei Longest Increasing subsequence
implementacja wkrótce

"""


def Ice_tower(T):
    n = len(T)
    dp = [0 for _ in range(n)]
    dp[0] = 1
    result = 0
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if T[j][1] > T[i][1] and T[j][0] < T[i][0]:
                dp[i] = max(dp[i], dp[j] + 1)
            result = max(result, dp[i])

    return result


# T = [
#     [0, 5],
#     [1, 4],
#     [-3, 7],
#     [2, 3],
#     [2, 6],
#     [4, 6],
#     [2, 3]
# ]

T = [(0, 10), (1, 10), (2, 6), (6, 7), (11, 20), (11, 19), (12, 18), (13, 19), (14, 20)]

print(Ice_tower(T))
