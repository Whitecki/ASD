# Zadanie 1. (kapitan statku, zadanie z kolokwium w 2012/13) Kapitan pewnego statku zastanawia
# się, czy może wpłynąć do portu mimo, że nastąpił odpływ. Do dyspozycji ma mapę zatoki w postaci tablicy
# M, gdzie M[y][x] to głebokość zatoki na pozycji (x, y). Jeśli jest ona większa niż pewna wartość int T
# to statek może się tam znaleźć. Początkowo statek jest na pozycji (0, 0) a port znajduje się na pozycji
# (n − 1, m − 1). Z danej pozycji statek może przepłynąć bezpośrednio jedynie na pozycję bezpośrednio obok
# (to znaczy, na pozycję, której dokładnie jedna ze współrzędnych różni się o jeden). Proszę napisać funkcję
# rozwiązującą problem kapitana.

def dfs(G, T):
    global time, visited,flag
    flag = False
    n = len(G)
    m = len(G[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    dfsVisit(G, T, 0, 0, n, m)
    return flag


def dfsVisit(G, T, kolumna, wiersz, n, m):
    global visited,flag
    visited[kolumna][wiersz] = True

    if kolumna == n - 1 and wiersz == m - 1:
        flag = True
        return True

    for i in range(1, -2, -1):
        if flag == True:
            return True

        if kolumna + i > -1 and kolumna + i < n:
            if abs(i) == 1:
                if not visited[kolumna + i][wiersz] and G[kolumna + i][wiersz] - T > 0:
                    dfsVisit(G, T, kolumna + i, wiersz, n , m)
            else:
                for j in range(-1, 2, 2):
                    if wiersz + j > -1 and wiersz + j < m:
                        if not visited[kolumna][wiersz + j] and G[kolumna][wiersz + j] - T > 0:
                            dfsVisit(G, T, kolumna, wiersz + j, n , m)


G = [[5,3,4,3,7,7,3],
     [7,3,6,3,3,7,3],
     [8,3,8,7,9,6,7],
     [4,3,5,3,10,3,7],
     [9,8,7,3,6,3,4]]

print(dfs(G,3))