from zad2testy import runtests
"""
puszczam algorytm poszukiwania pkt artykulacji, nastepnie z każdego puszczam dfs by sprawdzić spójność grafu"""

def DFS(G, points):
    V = len(G)
    parent = [None for _ in range(V)]
    visited = [False for _ in range(V)]
    d = [None for _ in range(V)]
    low = [None for _ in range(V)]
    time = 0

    def DFSVisit(G, u):
        nonlocal time
        time += 1
        d[u] = time
        low[u] = time
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFSVisit(G, v)

        for v in G[u]:
            if parent[u] != v:
                if low[v] < low[u]:
                    low[u] = low[v]
            if parent[v] == u:
                if low[v] < low[u]:
                    low[u] = low[v]

    for u in range(V):
        if not visited[u]:
            DFSVisit(G, u)

    childs = 0

    for v in G[0]:
        if parent[v] == 0:
            childs += 1

    if childs >= 2:
        points[0] = childs

    for u in range(1, V):
        cnt = 0
        for v in G[u]:
            if parent[v] == u:
                cnt += 1
                if low[v] >= d[u]:
                    points[u] += 1
        if points[u] == cnt and points[u] > 0:
            points[u] += 1


def art_points(G,n):
    points = [0 for _ in range(n)]

    DFS(G, points)
    return points


def breaking(G):
    n = len(G)
    GG = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]:
                GG[i].append(j)
    A = art_points(GG,n)
    result = max(A)
    if result == 0:
        return None
    return result


runtests( breaking )