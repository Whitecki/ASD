from queue import PriorityQueue
from math import inf

def Dijkstra(a,G):
    n = len(G)
    Q = PriorityQueue()
    Q.put((0, a))
    distance_a = [inf for i in range(n)]
    distance_a[a] = 0
    while not Q.empty():
        val, u = Q.get()
        for el in G[u]:
            v, w = el
            if val + w < distance_a[v]:
                distance_a[v] = val + w
                Q.put((distance_a[v], v))

    return distance_a

def dfsVisit(G, u,result,DTLN):
    if u == 1:
        return 1
    suma = 0
    for v,w in G[u]:
        if u > v and DTLN[u] < DTLN[v]:
            suma += dfsVisit(G, v, result,DTLN)
    return suma
def countRestrictedPaths(n, edges):

    #transform list of edges to list graph representation
    G = [[] for _ in range(n+1)]
    for (u,v,w) in edges:
        G[u].append([v,w])
        G[v].append([u,w])

    #dijkstra
    distanceToLastNode = Dijkstra(n,G)

    result = 0
    return dfsVisit(G, n, result,distanceToLastNode)

n = 9
edges = [[6,2,35129],[3,4,99499],[2,7,43547],[8,1,78671],[2,1,66308],[9,6,33462],[5,1,48249],[2,3,44414],[6,7,44602],[1,7,14931],[8,9,38171],[4,5,30827],[3,9,79166],[4,8,93731],[5,9,64068],[7,5,17741],[6,3,76017],[9,4,72244]]
print(countRestrictedPaths(n,edges))

