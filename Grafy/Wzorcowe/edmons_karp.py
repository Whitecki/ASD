from queue import Queue


def BFS(G, s, t, parent):
    V = len(G)
    Q = Queue()
    visited = [False for _ in range(V)]

    visited[s] = True
    Q.put(s)

    while not Q.empty():
        u = Q.get()

        for v in range(V):
            if not visited[v] and G[u][v] != 0:
                visited[v] = True
                parent[v] = u
                Q.put(v)

    return visited[t]


def edmons_karp(G, s, t):
    V = len(G)
    parent = [None for _ in range(V)]
    max_flow = 0

    while BFS(G, s, t, parent):
        min_flow = float('inf')
        u = t

        while u != s:
            min_flow = min(min_flow, G[parent[u]][u])
            u = parent[u]

        max_flow += min_flow
        v = t

        while v != s:
            u = parent[v]
            G[u][v] -= min_flow
            G[v][u] += min_flow
            v = u

    return max_flow