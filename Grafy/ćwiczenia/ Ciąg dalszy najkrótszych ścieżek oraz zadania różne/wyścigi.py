def DFS(G, d):
    V = len(G)
    visited = [False for _ in range(V)]
    time = 0

    def DFSVisit(G, visited, d, u):
        nonlocal time
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                DFSVisit(G, visited, d, v)

        time += 1
        d[u] = (time, u)

    for u in range(V):
        if not visited[u]:
            DFSVisit(G, visited, d, u)


def reverseGraph(G):
    V = len(G)
    G2 = [[] for _ in range(V)]

    for u in range(V):
        for v in G[u]:
            G2[v].append(u)

    return G2


def skladowe(G):
    V = len(G)
    d = [None for _ in range(V)]
    visited = [False for _ in range(V)]
    parts = []

    DFS(G, d)
    G2 = reverseGraph(G)

    d = sorted(d, reverse=True)

    def DFSVisit(G, visited, part, d, u, v):
        d[v] = (None, None)
        visited[u] = True
        part.append(u)

        for z in G[u]:
            if not visited[z]:
                for i in range(V):
                    if d[i][1] == z:
                        j = i
                        break
                DFSVisit(G, visited, part, d, z, j)

    for u in range(V):
        if d[u] != (None, None):
            part = []
            DFSVisit(G2, visited, part, d, d[u][1], u)
            parts.append(part)

    return parts


graph = [[1, 2],
         [2, 3],
         [0, 4],
         [4],
         [3]]

def dfs(A,G):
    visited = [False for _ in range(len(A))]
    def dfs_visit(s):
        visited[s] = True
        for el in G[s]:
            if not visited[el] and el in A:
                dfs_visit(el)
    dfs_visit(A[0])
    for el in A:
        if not visited[el]:
            return False
    return True

from copy import deepcopy
def race(G):
    G2 = deepcopy(G)
    A = skladowe(G)
    for el in A:
        if not dfs(el,G):
            return False

    return True
