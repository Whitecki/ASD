# Zadanie 5. (krawędzie 0/1) Dana jest mapa kraju w postaci grafu G = (V, E). Kierowca chce przejechać
# z miasta (wierzchołka) s to miasta t. Niestety niektóre drogi (krawędzie) są płatne. Każda droga ma taką 1
# samą jednostkową opłatę. Proszę podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczby
# opłat. W ogólności graf G jest skierowany, ale można najpierw wskazać algorytm dla grafu nieskierowanego.
from math import inf

def dfs(G,start,koniec):
    global dp,droga,parent
    n = len(G)
    dp = [inf for _ in range(n)]
    dp[start] = 0
    droga = []
    parent = [None for _ in range(n)]

    dfsVisit(G, start, koniec)

    if dp[koniec] == inf:
        return "cannot achive"
    i = koniec
    end = [koniec]
    while parent[i] != None:
            end.append(parent[i])
            i = parent[i]
    return end

def dfsVisit(G, start, koniec):
    global dp, droga
    droga.append(start)
    a = dp
    b = dp[koniec]

    m = len(G[start])
    for i in range(m):
        el = G[start][i][0]
        value = G[start][i][1]
        if dp[start] + value < dp[el]:
            dp[el] = dp[start] + value
            parent[el] = start
            if el != koniec:
                dfsVisit(G, el,koniec)


Graf = [[(1,1),(2,0)],
        [(0,1),(3,1),(4,1)],
        [(0,0),(3,1),(5,1)],
        [(1,1),(2,1),(4,0),(5,1)],#3
        [(1,1),(3,0),(6,1)],
        [(2,1),(3,1),(8,0)],#5
        [(4,1),(7,1),(9,1)],
        [(6,1),(8,1),(11,1)],
        [(5,0),(7,1),(10,0)], #8
        [(6,1),(11,1)],
        [(8,0),(11,0)],
        [(7,1),(9,1),(10,0)]]


print(dfs(Graf,start=0,koniec=11))
print(dp,parent)






