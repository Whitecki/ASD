from queue import PriorityQueue
from math import inf, log

def Dijkstra(a,G):
    n = len(G)
    Q = PriorityQueue()
    Q.put((0, a,-2))
    distance_a = [inf for _ in range(n)]
    parent = [-1 for _ in range(n)]
    distance_a[a] = 0
    while not Q.empty():
        val, u,tata = Q.get()
        for el in G[u]:
            v, w = el
            if val + w < distance_a[v]:
                distance_a[v] = val + w
                parent[v] = u
                Q.put((distance_a[v], v,u))
    return parent

def logartymy(G,u,v):
    for el in G:
        for g,e in el:
            e = log(e)
    result = [v]
    parent = Dijkstra(u,G)
    print(parent)
    i = v
    while i != u:
        result.append(parent[i])
        i = parent[i]
    result = result[::-1]

    return result

graph = [[(1, 20), (2, 30)],
         [(0, 20), (3, 12), (4, 11)],
         [(0, 30), (3, 18), (5, 2700)],
         [(1, 12), (2, 18), (8, 22), ],
         [(1, 11), (6, 15)],
         [(2, 2700), (7, 19), (8, 3)],
         [(4, 15), (8, 8)],
         [(5, 19)],
         [(3, 22), (5, 3), (6, 8)]]

u, v = 0, 7

print(logartymy(graph,u,v))