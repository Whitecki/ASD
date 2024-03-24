from zad3testy import runtests
from queue import PriorityQueue, Queue
from math import inf

def paths(G,s,t):
    """tu prosze wpisac wlasna implementacje"""
    PQ = PriorityQueue()
    PQ.put((0,s))
    n = len(G)
    distance = [inf for _ in range(n)]
    while not PQ.empty():
        d,u = PQ.get()
        if distance[u] == inf:
            distance[u] = d
            for v,w in G[u]:
                if distance[v] > distance[u] + w:
                    PQ.put((d + w, v))
    if distance[t] == inf:
        return 0
    Q = Queue()
    Q.put(t)
    cnt = -1
    visited = [False for _ in range(n)]
    while not Q.empty():
        u = Q.get()
        cnt += 1
        visited[u] = True
        for v,w in G[u]:
            if distance[v] + w == distance[u]:
                if not visited[v]:
                    visited[v] = True
                    Q.put(v)
                else:
                    cnt+= 1
    if cnt == 0:
        for v,w in G[s]:
         if v == t and w == distance[t]:
             return 1
    return cnt

    
runtests( paths )


