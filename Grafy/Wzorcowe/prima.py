from queue import PriorityQueue


def Prima(G):
    V = len(G)
    DQ = PriorityQueue()
    W = [float('inf') for _ in range(V)]
    visited = [False for _ in range(V)]
    parent = [None for _ in range(V)]

    W[0] = 0
    DQ.put((W[0], 0))

    while not DQ.empty():

        _, u = DQ.get()

        if not visited[u]:

            visited[u] = True

            for v, w in G[u]:
                if W[v] > w and parent[u] != v:
                    parent[v] = u
                    W[v] = w
                    DQ.put((W[v], v))

    MST = []

    for u in range(1, V):
        MST.append((parent[u], u))

    return MST
