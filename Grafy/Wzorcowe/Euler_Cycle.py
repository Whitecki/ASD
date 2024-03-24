def is_eulerCycle(G):
    for i in range(len(G)):
        if len(G[i]) % 2 != 0:
            return False
    return True


def remove(G, u, v):
    for i in range(len(G[v])):
        if G[v][i] == u:
            G[v][i] = None
            break

    for i in range(len(G[u])):
        if G[u][i] == v:
            G[u][i] = None
            break


def DFS(G, M, u):
    for v in G[u]:
        if v is not None:
            remove(G, u, v)
            DFS(G, M, v)

    M.append(u)


def eulerCycle(G):
    M = []
    DFS(G, M, 0)
    return M


########################
class vis:
    def __init__(self, vis):
        self.visited = vis


AdjList = [[] for i in range(11)]


def AddEdge(G, u, v, w=0):
    visited = vis(False)
    G[u].append([v, w, visited])
    G[v].append([u, w, visited])


AddEdge(AdjList, 0, 1)
AddEdge(AdjList, 1, 3)
AddEdge(AdjList, 3, 5)
AddEdge(AdjList, 1, 2)
AddEdge(AdjList, 0, 3)
AddEdge(AdjList, 3, 8)
AddEdge(AdjList, 5, 7)
AddEdge(AdjList, 7, 10)
AddEdge(AdjList, 6, 8)
AddEdge(AdjList, 6, 9)
AddEdge(AdjList, 4, 9)
AddEdge(AdjList, 1, 4)
AddEdge(AdjList, 2, 10)


def FindEulerCycle(G):
    if (IsEulerCycle(G) == False):
        return False
    path = []

    def DFSVisit(start):
        nonlocal path
        for i in range(len(G[start])):
            if (G[start][i][2].visited == False):
                G[start][i][2].visited = True
                DFSVisit(G[start][i][0])
                path.append(G[start][i][0])

    for i in range(len(G)):
        DFSVisit(i)
    return path


def IsEulerCycle(G):
    n = len(G)
    for i in range(n):
        if (len(G[i]) % 2 != 0):
            return False
    visited = [False for _ in range(n)]
    time = 0

    def DFSVisit(G, start):

        nonlocal time
        nonlocal visited
        time += 1
        visited[start] = True
        for i in G[start]:
            if (visited[i[0]] == False):
                DFSVisit(G, i[0])

    DFSVisit(G, 0)
    return time == n


print(FindEulerCycle(AdjList))