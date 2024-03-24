# Given a Directed Graph, find a Mother Vertex in the Graph (if present).
# A Mother Vertex is a vertex through which we can reach all the other vertices of the Graph.

'''
idea:
time complexity:O(V+E)
'''


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

def TS(G):
    visited = [False for _ in range(len(G))]
    result = []
    for idx in range(len(G)):
        if not visited[idx]:
            dfsVisit(True,G, idx,result,visited)
    result = result[::-1]
    return result

def Mother_of_Vertex(G):

    M, help = SCC(G)
    a = TS(M)[0]
    i = 0
    result = []
    visited = [False for _ in range(len(G))]
    while i < (len(G)):
        if help[i] == a:
            break
        i += 1
    dfsVisit(True,G,i,result,visited)
    if len(result) == len(G):
        return i
    return False

