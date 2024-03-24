from queue import Queue

def dfs(G):
    n = len(G)
    d = [-1 for _ in range(n)]
    low = [-1 for i in range(n)]
    parent = [-1 for _ in range(n)]
    ArticulationPts = []
    cnt = 1
    def dfsVisit(G, s, d, low, parent, ArticulationPts):
        global cnt
        d[s] = cnt
        low[s] = cnt
        cnt += 1
        children = 0
        for el in G[s]:
            if d[el] == -1:
                parent[el] = s
                children += 1
                dfsVisit(G, s, d, low, parent, ArticulationPts)

                low[s] = min(low[s], low[el])
                # s jest root-em drzewa i ma więcej niż jedno dziecko => pkt artykulacji
                if parent[s] == -1 and low[el] >= d[s]:
                    ArticulationPts.append(s)
                if parent[s] != -1 and low[el] >= d[s]:
                    ArticulationPts.append(s)
            elif el != parent[s]:
                low[s] = min(low[s], low[el])

    dfsVisit(G, 0, d, low, parent, ArticulationPts)
    return ArticulationPts


###########################

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
        points.append(0)

    for u in range(1, V):
        for v in G[u]:
            if parent[v] == u and low[v] >= d[u]:
                points.append(u)
                break


def art_points(G):
    points = []

    DFS(G, points)

    return points
