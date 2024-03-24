# tradycyjny bfs, nawet nie ma co pisać

from queue import Queue

def BFS(G, s):
    Q = Queue()
    n = len(G)
    visited = [False for _ in range(n)]
    cnt = [0 for _ in range(n)]
    visited[s] = True
    Q.put((s, 0))
    while not Q.empty():
        u, c = Q.get()
        cnt[c] += 1
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                Q.put(v)
    maxi = 0
    idx = 0
    for i in range(n):
        if cnt[i] > maxi:
            idx, maxi = i, cnt[i]
    return maxi, idx
