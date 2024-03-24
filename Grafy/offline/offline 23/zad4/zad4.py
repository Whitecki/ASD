from zad4testy import runtests
from queue import Queue
from math import inf
from random import randint
# def longer( G, s, t ):
#     n = len(G)
#     # (i,G[i][j])
#     last = -1
#     for i in range(n):
#         for j in range(len(G[i])):
#             a, b = (i, G[i][j]), (G[i][j], i)
#             Q = Queue()
#             Dist = [inf for _ in range(n)]
#             Dist[s] = 0
#             Q.put(s)
#             while not Q.empty():
#                 u = Q.get()
#                 for v in G[u]:
#                     if Dist[v] > Dist[u] + 1 and (u,v) != a and  (u,v) != b:
#                         Q.put(v)
#                         Dist[v] = Dist[u] + 1
#             if Dist[t] > last and last > -1:
#                 return a
#             last = Dist[t]
#     return None







def Bridge(G,Boll,s):
    bridges = []

    V = len(G)
    visited = [False for _ in range(V)]
    parent = [None for _ in range(V)]
    d = [None for _ in range(V)]
    low = [None for _ in range(V)]
    time = 0

    def DFSVisit(G, visited, parent, bridges, d, u):
        nonlocal time
        time += 1
        d[u] = time
        low[u] = d[u]
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFSVisit(G, visited, parent, bridges, d, v)

        for v in G[u]:
            if Boll[v] and v != -1:
                if parent[v] == u:
                    if low[v] < low[u]:
                        low[u] = low[v]
                if v != parent[u]:
                    if low[v] < low[u]:
                        low[u] = low[v]

        if low[u] == d[u] and parent[u] is not None:
            bridges.append((u, parent[u]))

    DFSVisit(G, visited, parent, bridges, d, s)

    return bridges

def longer( G, s, t ):
    # oznaczam wierzchołki które należą do podgrafu, najkrótszej ścieżki z s do t
    Q = Queue()
    n = len(G)
    Dist = [inf for _ in range(n)]
    Dist[s] = 0
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if Dist[v] > Dist[u] + 1:
                Q.put(v)
                Dist[v] = Dist[u] + 1
    Bool = [False for _ in range(n)]
    if Dist[t] == inf: return None
    # oznaczam wierzchołki które należą do podgrafu, najkrótszej ścieżki z s do t
    Bool[t] = True
    Q.put(t)

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if Dist[u] - 1 == Dist[v]:
                Q.put(v)
                Bool[v] = True

    to = [-1 for i in range(n)]
    a = 0
    lenn = [len(G[i]) for i in range(n)]
    for i in range(n):
        if Bool[i]:
            to[i] = a
            a += 1
            for j in range(lenn[i]):
                if not Bool[G[i][j]]:
                    G[i][j] = -1
                    lenn[i] -= 1
        else:
            G[i] = []
    GG = []
    for i in range(n):
        if Bool[i]:
            helper = [-1 for _ in range(lenn[i])]
            j = 0
            while j < len(G[i]):
                if G[i][j] != -1:
                    helper[lenn[i]-1] = to[G[i][j]]
                    lenn[i] -= 1
                j+= 1
            GG.append(helper)

    # trzeba sprawdzać czy wierzchołek istnieje i czy istnieje krawędź z/do niego
    a = Bridge(GG, Bool, s)
    a1,a2 = a[0] #randint(0,len(a)-1)
    b1,b2 = False,False
    i = 0
    while not b1 * b2:
        if to[i] ==a1 and not b1:
            a1 = i
            b1 = True
        if to[i] == a2 and not b2:
            a2 = i
            b2 = True
        i+=1

    Dis = [inf for _ in range(n)]
    Dis[s] = 0
    B = Queue()
    B.put(s)
    while not B.empty():
        u = B.get()
        for v in GG[u]:
            if Dis[v] > Dis[u] + 1 and (u,v) != (a1,a2) and (u,v) != (a2,a1):
                B.put(v)
                Dis[v] = Dis[u] + 1
    if Dist[t] == Dis[t]:
        return None
    return (a1,a2)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )