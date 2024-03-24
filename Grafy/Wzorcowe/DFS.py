def dfs(G):
    visited = [False for _ in range(len(G))]
    result = []
    for idx in range(len(G)):
        if not visited[idx]:
            dfsVisit(G, idx,result,visited)
    return result

def dfsVisit(G, s,result,visited):
    result.append(s)
    visited[s] = True

    for el in G[s]:
        if not visited[el]:
            dfsVisit(G, el,result,visited)

G = [[1,4],
     [0,2],
     [1,3,5],
     [2,4,6],
     [0,3,5],
     [2,4],
     [3,7],
     [6]]

print(dfs(G))
from queue import Queue
#może działająca iteracyjna wersja,tylko trzeba użyć stosu, a nie kolejki
def DFS(G):
    n = len(G)
    d = [-1 for _ in range(n)]
    d[0] = 0
    Q = Queue()
    Q.put(0)
    cnt = 1
    while not Q.empty():
        u = Q.get()
        for el in G[u]:
            if d[el] != -1:
                Q.put(el)
                d[el] = cnt
                cnt += 1