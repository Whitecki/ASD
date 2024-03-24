#w zadaniu zakładamy, że długość samochodów to liczby naturalne
def tytanic(A:"tablica z długościami samochodów",L:"długość obu pasów na samochody"):
    n = len(A)
    #dp[i][l][r] - udało się postawić i-ty samochód i pozostało wolnego miejsca kolejno l i r na obu pasach
    dp = [[[0 for _ in range(L+1)] for _ in range(L+1)] for _ in range(n)]
    for i in range(n):
        for l in range(A[i],L+1):
            for r in range(A[i],L+1):
                dp[i][l][r] = max(dp[i-1][l-A[i]][r] + 1, dp[i-1][l][r-A[i]] + 1)
    return n# wszystkie wjechały


A = [1, 1, 2, 3, 5, 8, 13]
L = 8
# L = 18.24
# cars = [15.16, 7.23, 4.98, 2.11, 3.08, 3.92, 6.34, 4.39, 2.63, 1234.88]
# L = int(L*100)
# for i in range(len(cars)):
#     cars[i] = int(cars[i]*100)

print(tytanic(A,L))


from math import inf


def cars_on_ferry(A, L):
    n = len(A)
    DP = [[[-inf] * (L + 1) for _ in range(L + 1)] for _ in range(n)]
    for i in range(L):
        for j in range(L):
            DP[0][i][j] = 0
    return solution(A, DP, 0, L, L)


def solution(A, DP, i, j, k):
    if DP[i][j][k] != -inf:
        return DP[i][j][k]
    a = b = 0
    if A[i] <= j:
        a = solution(A, DP, i + 1, j - A[i], k) + 1
    if A[i] <= k:
        b = solution(A, DP, i + 1, j, k - A[i]) + 1
    DP[i][j][k] = max(a, b)
    return DP[i][j][k]


A = [1, 1, 2, 3, 2, 8, 13]
L = 8
print(cars_on_ferry(A, L))
