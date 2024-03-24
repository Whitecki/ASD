# Proszę podać i zaimplementować algorytm znajdujący wartość optymalnego zbioru
# przedmiotów w dyskretnym problemie plecakowym.Algorytm powinien działać w czasie
# wielomianowym względem liczby przedmiotów oraz sumy ich profitów.

# M - masa i-tego przedmiotu
# W - wartość i-tego przedmiotu
# c - maksymalny ciężar jaki mogę unieść

def plecak(M,W,c):

    # tabelka udzwigu od elementów
    n = len(M)
    DP = [[0 for i in range(c+1)] for _ in range(n)]

    for i in range(W[0],n):
        DP[0][i] = W[0]

    for i in range(c+1):
        for j in range(1,n):

            DP[i][j] = DP[i-1][j]

            if M[i] <= j:

                DP[i][j] = max(DP[i - 1][j], DP[i-1][j - M[i]] + W[i])

    return DP[n-1][c]



