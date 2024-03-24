from zad1testy1920popr import runtests
from queue import PriorityQueue
from math import inf

def transform(G,n):
    A = [[]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != -1:
                A[i].append((j,G[i][j]))
    return A

def jak_dojade(A, P,d: 'capacity of car\'s fuel tank', a, b):
    # zamieniamy forme grafu
    n = len(A)
    G = transform(A,n)
    #dijkstra na rozmnozonych wierzchołkach
    tankowanie = [False for _ in range(n)]
    for el in P:
        tankowanie[el] = True
    visited = [[[inf,-1] for _ in range(d+1)] for _ in range(n)]
    Q = PriorityQueue()
    Q.put((0,a,d,None))
    while not Q.empty():
        dist,u,paliwo,tata = Q.get()
        if tankowanie[u]:
            paliwo = d
        if visited[u][paliwo][0] > dist: # jeżeli już jakiś samochód nie wystartował z tego wierzchołka z taką ilością paliwa
            for v,w in G[u]:
                if w <= paliwo and visited[v][paliwo - w][0] > dist + w:
                    Q.put((dist + w,v,paliwo - w,u))
            visited[u][paliwo][0] = dist
            visited[u][paliwo][1] = tata

    parent = [-1 for _ in range(n)]

    for vert in range(n):
        minimum, idx = inf, -1
        for i in range(d+1):
            if minimum > visited[vert][i][0]:
                minimum = visited[vert][i][0]
                idx = i
        parent[vert] = visited[vert][idx][1]

    result = [b]
    # i = b
    # while i != a:
    #     if tankowanie[i]:
    #         i = visited[i][d][1]
    #     else:
    #         i = visited[b][idx - ][1]
    #
    #     result.append(i)
    return result
## trzeba dokończyc odtwarzanie ścieżki
runtests(jak_dojade)