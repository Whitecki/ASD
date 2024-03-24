from zad6testy import runtests
from queue import Queue
from math import inf

# samodzielna implementacja algorytmu Hopcroft–Karp
# Algorytm wyszukuje maksymalną wartość skojarzeń w grafie dwudzielnym.
# time complexity: ElogV

def BFS(U,G,NIL,Dist,Pair_V,Pair_U):
    Q = Queue()
    for u in U:
        if Pair_U[u] == NIL:
            Dist[u] = 0
            Q.put(u)
        else:
            Dist[u] = inf
    Dist[NIL] = inf
    while not Q.empty():
        u = Q.get()
        if Dist[u] < Dist[NIL]:
            for v in G[u]:
                if Dist[Pair_V[v]] == inf:
                    Dist[Pair_V[v]] = Dist[u] + 1
                    Q.put(Pair_V[v])
    return Dist[NIL] != inf

def DFS(u,G,NIL,Dist,Pair_V,Pair_U):
    if u != NIL:
        for v in G[u]:
            if Dist[Pair_V[v]] == Dist[u] + 1:
                if DFS(Pair_V[v],G,NIL,Dist,Pair_V,Pair_U):
                    Pair_V[v] = u
                    Pair_U[u] = v
                    return True
        Dist[u] = inf
        return False
    return True


def binworker( M ):
    n = len(M)
    NIL = n
    U = [i for i in range(n)]
    Dist = [0 for _ in range(n+1)]
    Pair_U = [NIL for _ in range(n+1)]
    Pair_V = [NIL for _ in range(n+1)]
    matching = 0
    while BFS(U,M,NIL,Dist,Pair_V,Pair_U):
        for u in U:
            if Pair_U[u] == NIL and DFS(u,M,NIL,Dist,Pair_V,Pair_U):
                matching += 1
    return matching

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = False )
