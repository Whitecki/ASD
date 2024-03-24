# Zadanie 4. (malejące krawędzie) Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru
# {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych wierzchołków
# x i y sprawdza, czy istnieje ścieżka z x do y, w której przechodzimy po krawędziach o coraz mniejszych wagach.
from math import inf


def dfsVisit(G, s, y, droga):
    global time, visited, wynik, waga
    # doszliśmy do końca
    if s == y or wynik:
        wynik = True
        return True

    droga.append(s)
    visited[s] = True
    m = len(G[s])
    # bierzemy każdą krawędź z wierzchołka s
    for i in range(m):
        el = G[s][i][0]
        value = G[s][i][1]

        # idziemy przez nieodwiedzone i z mniejszą wartością krawędzie
        if not visited[el] and value < waga:
            waga = value
            if dfsVisit(G, el, y, droga):
                return True

    # cofamy się o jeden wierzchołek i przywracamy poprzednią wagę
    del droga[-1]
    if len(droga) > 1:
        o = len(G[droga[-1]])
        for i in range(o):
            if droga[-2] == G[droga[-1]][i][0]:
                waga = G[droga[-1]][i][1]
    else:
        waga = inf


def dfs(G, x, y):
    global visited, time, wynik, waga
    wynik = False
    visited = [False for _ in range(len(G))]
    time = 0
    waga = inf
    droga = []
    dfsVisit(G, x, y, droga)
    return wynik
    #
    # for idx in range(len(G)):
    #     if not visited[idx]:
    #         dfsVisit(G, idx)


Graf = [[(1, 12), (2, 7)],
        [(0, 12), (3, 13), (4, 9)],
        [(0, 7), (3, 2), (5, 4)],
        [(1, 13), (2, 2), (4, 10), (5, 3)],
        [(1, 9), (3, 13), (6, 10)],
        [(2, 4), (3, 3), (6, 2)],
        [(4, 10), (5, 2)]]
if dfs(Graf, 0, 6):
    print("sukces")

else:
    print("chuj")
