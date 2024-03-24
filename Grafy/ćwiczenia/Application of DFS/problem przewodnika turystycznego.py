from queue import PriorityQueue
from math import inf, ceil

def Dijkstra(a,b,G):
    n = len(G)
    Q = PriorityQueue()
    Q.put((0, a))
    distance_a = [0 for _ in range(n)]
    distance_a[a] = inf
    while not Q.empty():
        val, u = Q.get()
        val*=-1
        for el in G[u]:
            v, w = el
            if min(distance_a[u],w) > distance_a[v]:
                distance_a[v] = min(distance_a[u],w)
                Q.put((-1*distance_a[v], v))
    return distance_a[b]

def Guide(E,k,a,b):
    n = 0
    for x,y,c in E:
        n = max(x,y,n)
    G = [[] for _ in range(n+1)]

    for x,y,c in E:
        G[x].append([y,c])
        G[y].append([x,c])

    m = Dijkstra(a,b,G)
    return ceil(k/m)

C = [(0, 1, 8), (0, 2, 15), (0, 5, 12), (0, 10, 10), (0, 12, 30), (1, 4, 15), (1, 2, 4), (2, 3, 7), (3, 1, 10),
     (3, 4, 13), (4, 7, 14), (5, 6, 20), (5, 3, 18), (6, 4, 11), (6, 7, 8), (8, 7, 4), (9, 8, 12), (10, 5, 19),
     (10, 11, 25), (10, 7, 10), (11, 9, 60), (12, 11, 32), (9, 10, 25)]

num_tourists = 100
s = 0
t = 3

print(Guide(C,num_tourists,s,t))