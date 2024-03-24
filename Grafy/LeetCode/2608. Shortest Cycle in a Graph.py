from queue import Queue
from math import inf

#algorytm wykrywa długość cyklu, wystarczy na podstawie parentów odtworzyć te scieżkę:))


def BFS(G):
    Q = Queue()
    n = len(G)
    visited = [[[inf,None] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        Q.put((i,0,i,None))
    minimal = inf
    while not Q.empty():
        u,d,i,parent = Q.get()
        visited[i][u][0] = d
        visited[i][u][1] = parent
        if d >= minimal: break
        for v in G[u]:
            if inf == visited[i][v][0]:
                Q.put((v,d+1,i,u))
            if visited[i][v][0] != inf and parent != v:
                minimal = min(minimal,d+1+visited[i][v][0])
    j = []

    if minimal != inf:
        return minimal
    return -1



G = [[1,2],
     [2,0],
     [0,1],
     [4,6],
     [3,5],
     [4,6],
     [3,5]]

print(BFS(G))