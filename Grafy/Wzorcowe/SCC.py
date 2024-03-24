
def SCC(G):
    visited = [False for _ in range(len(G))]
    result = []
    for idx in range(len(G)):
        if not visited[idx]:
            dfsVisit(True, G, idx, result, visited)
    S = [[] for _ in range(len(G))]

    # odwracam kierunek krawędzi
    for i in range(len(G)):
        for a in G[i]:
            S[a].append(i)

    # odpalam dfs po najwyższym czasie przetworzenia
    visited = [False for _ in range(len(G))]
    help = [_ for _ in range(len(G))]
    i = -1
    result = result[::-1]
    for el in result:
        if not visited[el]:
            i += 1
            dfsVisit(False, S, el, (help, i), visited)

    # przetwarzam graf do DAG-u
    M = [[] for _ in range(i+1)]
    is_connected = [[False for _ in range(len(G))] for _ in range(len(G))]
    for idx in range(len(G)):
        for el in G[idx]:
            if help[idx] != help[el] and not is_connected[help[idx]][help[el]]:
                M[help[idx]].append(help[el])
                is_connected[help[idx]][help[el]] = True

    return M, help


def dfsVisit(flag, G, s, q, visited):
    visited[s] = True
    if not flag:
        q[0][s] = q[1]
    for el in G[s]:
        if not visited[el]:
            if not flag:
                q[0][el] = q[1]
                dfsVisit(False,G, el, q, visited)
            else:
                dfsVisit(True, G, el, q, visited)
    if flag:
        q.append(s)

G = [[1,8],
     [2],
     [0,6],
     [4],
     [5,7],
     [6,9],
     [3],
     [8,10],
     [9],
     [7],
     [9]]

print(SCC(G))
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