class Node:
    def __init__(self,next):
        self.next = next

def euler(G):
    visited = [False for _ in range(len(G))]
    result = []
    słownik = {}
    for idx in range(len(G)):
        if not visited[idx]:
            dfsVisit(G, idx,result,visited)
    return result

def dfsVisit(G, s,result,visited):
    visited[s] = True

    for el in G[s]:
        if not visited[el]:
            dfsVisit(G, el,result,visited)









def DFSaddCycle(G,v,w,p,visited):
    visited[w] = True
    p.append(w)
    for u in G[w]:
        if not u != v: #znaleźlismy wierzchołek startowy cyklu
            p.append(u)


def Euler_cycle(graf):
    n = len(graf)
    C = []
    visited = [False for _ in range(n)]
    for i in range(n):
        if len(graf[i]) != 0:

