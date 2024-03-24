def DFS(G, bridges):
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
            if parent[v] == u:
                if low[v] < low[u]:
                    low[u] = low[v]
            if v != parent[u]:
                if low[v] < low[u]:
                    low[u] = low[v]

        if low[u] == d[u] and parent[u] is not None:
            bridges.append((u, parent[u]))

    for u in range(V):
        if not visited[u]:
            DFSVisit(G, visited, parent, bridges, d, u)


def bridge(G):
    V = len(G)
    bridges = []

    DFS(G, bridges)

    return bridges


G = [[1, 4], [2,0], [3,1], [2, 5], [5,0], [3,4]]

print(bridge(G))