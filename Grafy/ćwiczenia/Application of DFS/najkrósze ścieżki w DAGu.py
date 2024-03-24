def TS(G):
    visited = [False for _ in range(len(G))]
    result = []
    for idx in range(len(G)):
        if not visited[idx]:
            dfsVisit(G, idx,result,visited)
    result = result[::-1]
    return result
def dfsVisit(G, s,result,visited):
    visited[s] = True

    for el in G[s]:
        if not visited[el]:
            dfsVisit(G, el,result,visited)
    result.append(s)

G = [[1,2,5],
     [2,4],
     [],
     [],
     [3,6],
     [4],
     []]


from queue import Queue
from math import inf

def BFS(G,s):
    Q = Queue()
    n = len(G)
    visited = [0 for _ in range(n)]
    Q.put((s,0))
    while not Q.empty():
        u,w = Q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = w + 1
                Q.put((v,w+1))
    for i in range(len(G)):
        if not visited[i] and i != s:
            visited[i] = inf
    return visited


def Dawid(G,s):
    n = len(G)
    # A = TS(G)
    # czy_po_prawo = [-1 for _ in range(n)]
    #
    # flag = False
    # for i in range(n):
    #     if A[i] == s:
    #         flag = True
    #     czy_po_prawo[i] = flag

    return BFS(G,s)

G = [[1, 2],
    [2, 3, 5],
    [4, 3],
    [5, 4],
    [5],
    []]

print(Dawid(G,0))