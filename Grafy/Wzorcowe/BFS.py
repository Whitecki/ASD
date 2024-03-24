from queue import Queue

def BFS(G,s):
    Q = Queue()
    n = len(G)
    visited = [False for _ in range(n)]
    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                Q.put(v)

    return