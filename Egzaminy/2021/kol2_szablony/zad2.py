from zad2testy import runtests
from queue import Queue
from math import inf


def bfs(G, s, n):
    Q = Queue()
    visited = [False for _ in range(n)]
    time = [inf for _ in range(n)]
    time[s] = 0
    Q.put((s, 1))
    while not Q.empty():
        u, t = Q.get()
        if not visited[u]:
            time[u] = t
            visited[u] = True
            for v in G[u]:
                if not visited[v]:
                    Q.put((v, t + 1))
    return time

def DFS(G,bridges):
    V = len(G)
    visited = [False for _ in range(V)]
    parent = [None for _ in range(V)]
    d = [None for _ in range(V)]
    low = [None for _ in range(V)]
    time = 0
    def DFSVisite(G,visited,parent,bridges,d,u):
        nonlocal time
        time += 1
        d[u] = time
        low[u] = d[u]
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFSVisite(G,visited,parent,bridges,d,v)

        for v in G[u]:
            if parent[v] == u:
                if low[v] < low[u]:
                    low[u] = low[v]
            if parent[u] != v:
                if low[v] < low[u]:
                    low[u] = low[v]
        if low[u] == d[u] and parent[u] is not None:
            bridges.append((u,parent[u]))

    for u in range(V):
        if not visited[u]:
            DFSVisite(G,visited,parent,bridges,d,u)

def bridge(G):
    V = len(G)
    bridges = []
    DFS(G,bridges)
    return bridges

def enlarge(G, s, t):
    # Zmieniam reprezentację na listę sąsiedztwa
    n = len(G)
    # A = [[] for _ in range(n)]
    # for x,y in G:
    #     A[x].append(y)
    #     A[y].append(x)
    # odpalam bfs by miec kolejnosć odwiedzin z p
    time = bfs(G, s, n)
    if time[t] == inf:
        return None
    # wyruszam z q i idę po wierzchołakch o mniejszych wagach
    B = [[] for _ in range(n)]
    Q1 = Queue()
    Q1.put(t)
    while not Q1.empty():
        u = Q1.get()
        for v in G[u]:
            if time[v] + 1 == time[u]:
                Q1.put(v)
                B[u].append(v)
                B[v].append(u)

    # odpalam algorytm na wyszukiwanie mostów
    result = bridge(B)
    if len(result) != 0:
        if result[0][0] < result[0][1]:
            return result[0]
        else:
            return (result[0][1],result[0][0])
    return None


runtests(enlarge)
