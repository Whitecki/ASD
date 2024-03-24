from queue import Queue
from math import inf


def bfs(graph, s, t, parent):
    queue = Queue()
    visited = [False] * len(graph)
    visited[s] = True
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] != 0:
                visited[v] = True
                parent[v] = u
                queue.put(v)
    return visited[t]


def edmonds_karp_algorithm(graph, s, t):
    parent = [None] * len(graph)
    max_flow = 0
    while bfs(graph, s, t, parent):
        current_flow = inf
        current = t
        while current != s:
            current_flow = min(current_flow, graph[parent[current]][current])
            current = parent[current]
        max_flow += current_flow
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= current_flow
            graph[v][u] += current_flow
            v = parent[v]
    return max_flow


def apps_and_comps(A, K, clients):  # komputery maja numerki A,...,A + K
    # A - lista aplikacji polaczonych z komputerami - losta saiedztwa
    # clients - lista 'ile klientow chce skorzytsac z i-tej apki'
    res = 0
    for i in range(len(clients)):
        res += clients[i]
    a = len(A)
    G = [[0 for _ in range(a + K + 2)]]
    for i in range(1, 1 + a):
        G[0][i] = G[i][0] = clients[i - 1]
    for k in range(K):
        G[a + K + 1][k] = G[k][a + K + 1] = 1
    for i in range(a):
        for j in A[i]:
            G[i + 1][j] = 1
            G[j][i + 1] = 1  # zalozmy ze macierz jest dobrz ezrobiona

    if edmonds_karp_algorithm(G, 0, a + K + 1) == res:
        return True
    return False

# generalnie wiem ocb, ale karp jest tutaj chyba na listach, a algorytm ma macierzowa
