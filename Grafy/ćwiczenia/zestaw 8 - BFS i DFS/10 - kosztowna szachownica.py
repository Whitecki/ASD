# Zadanie 7. (kosztowna szachownica) Dana jest szachownica o wymiarach n × n. Każde pole (i, j)
# ma koszt (liczbę ze zbioru {1, . . . , 5}) umieszczony w tablicy A (na polu A[j][i]). W lewym górnym rogu
# szachownicy stoi król, którego zadaniem jest przejsc do prawego dolnego rogu, przechodzac po polach o
# minmalnym sumarycznym koszcie. Prosze zaimplementowac funkcje kings path(A), która oblicza koszt
# sciezki króla. Funkcja powinna byc mozliwie jak najszybsza.

from math import inf


def dfs(G):
    # robimy dynamika
    n = len(G)
    global dp
    dp = [[inf for _ in range(n)] for _ in range(n)]
    dp[0][0] = G[0][0]

    #odpalamy rekurencje
    dfsVisit(G, 0, 0, n)

    # zwracamy koszt dojścia do końca
    return dp[n - 1][n - 1]


def dfsVisit(G, wiersz, kolumna, n):

    # warunek wyjścia poza tablice
    moves = [-1, 0, +1]
    for j in moves:
        if kolumna + j > -1 and kolumna + j < n:
            for i in moves:
                if wiersz + i > -1 and wiersz + i < n:

                    #sprawdzamy czy opłaca się przeskakiwać, w nowe miejsce
                    value = G[kolumna + j][wiersz + i]
                    if dp[kolumna][wiersz] + value < dp[kolumna + j][wiersz + i]:
                        dp[kolumna + j][wiersz + i] = dp[kolumna][wiersz] + value

                        # nie wskakujemy na nasz końcowy cel
                        if i != n - 1 and j != n - 1:
                            dfsVisit(G, wiersz + i, kolumna + j, n)


Graf = [[3, 2, 1, 5],
        [2, 5, 4, 2],
        [1, 2, 5, 5],
        [2, 4, 2, 3]]

print(dfs(Graf))
print(dp)
