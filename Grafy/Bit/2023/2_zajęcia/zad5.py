'''
odpalam dijkstre, odtwarzam ścieżkę jaką przeszedł
odpalam bfs, zapamiętując czas przetworzenia
Sprawdzam czy każdy kolejny wierzchołek należał do następnej "fali"(miał większy czas
przetworzernia o 1) :)))
'''

from queue import Queue, PriorityQueue
from math import inf

def BFS(G,s):
    Q = Queue()
    n = len(G)
    visited = [0 for _ in range(n)]
    Q.put((s,1))
    while not Q.empty():
        u,d = Q.get()
        if not visited[u]:
            visited[u] = d
            for v,w in G[u]:
                if not visited[v]:
                    Q.put((v,d+1))
    return visited

def Dijkstra(G,poczatek,koniec):
    Q = PriorityQueue()
    n = len(G)
    visited = [inf for _ in range(n)]
    parent = [-1 for i in range(n)]
    Q.put((0, poczatek, None))
    while not Q.empty():
        dist,u,tata = Q.get()
        if visited[u] == inf:
            visited[u] = dist
            parent[u] = tata
            for v,w in G[u]:
                if dist + w < visited[v]:
                    Q.put((dist + w,v,u))
    # odtwarzamy ścieżkę
    result = [koniec]
    i = koniec
    while parent[i] is not None:
        i = parent[i]
        result.append(i)
    result.reverse()
    return result

def superfajne(G,poczatek,koniec):
    numeracja = BFS(G,poczatek)
    nwm = Dijkstra(G,poczatek,koniec)
    for i in range(len(nwm)):
        nwm[i] = numeracja[nwm[i]]
    for i in range(1,len(nwm)):
        if nwm[i-1] + 1 != nwm[i]:
            return False
    return True

G = [[[2,40]],
     [[2,100],[3,60]],
     [[0,40],[1,100],[3,80]],
     [[1,60],[2,80]]]
print(superfajne(G,0,1))