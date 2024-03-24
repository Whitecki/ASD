from zad1testy import runtests
from queue import Queue
#O(v**4)

def z_kazdego_do_kazdego(G):
    n = len(G)
    D = [[float('inf') for _ in range(n)] for _ in range(n)]
    parent = [[None for _ in range(n)] for _ in range(n)]

    for u in range(n):
        for v in range(n):
            if u == v:
                D[u][v] = 0
            elif G[u][v] != 0:
                D[u][v] = G[u][v]
                parent[u][v] = u

    for i in range(n):
        for u in range(n):
            for v in range(n):
                if D[u][v] > D[u][i] + D[i][v]:
                    D[u][v] = D[u][i] + D[i][v]
                    parent[u][v] = parent[i][v]
    return D


def keep_distance(M, x, y, d):
    n = len(M)
    GG = [[]]  # lista sąsiedztwa zrobiona z M
    D = z_kazdego_do_kazdego(M)
    G = [[] for _ in range(n ** 2)]
    gdzie_juz_bylo = [[-1 for _ in range(n)] for _ in range(n)]  # gdzie wystepuje punkt(i,j) w G
    gdzie_juz_bylo[x][y] = 0
    parent = [-1 for _ in range(n**2)]
    parent[0] = None
    # tworze graf O(V**4)
    cnt = 0
    Q = Queue()
    Q.put((x,y))
    warstwa = 1
    r = -1
    while not Q.empty():
        a, b = Q.get()
        if a == y and b == x:
            r = gdzie_juz_bylo[a][b]
            break
        for i in range(3):  # idze x, idzie y, idą obaj
            if i == 0:
                for u in GG[a]:
                    if D[u][b] >= d and gdzie_juz_bylo[u][b] == -1:
                        G[gdzie_juz_bylo[a][b]].append(warstwa)
                        gdzie_juz_bylo[u][b] = warstwa
                        Q.put((u, b))
                        warstwa += 1
            if i == 1:
                for v in GG[b]:
                    if D[a][v] >= d and not gdzie_juz_bylo[a][v]:
                        G[gdzie_juz_bylo[a][b]].append(warstwa)
                        gdzie_juz_bylo[a][v] = warstwa
                        Q.put((a, v))
                        warstwa += 1
            if i == 2:
                for u in GG[a]:
                    for v in GG[b]:
                        if D[u][v] >= d and not gdzie_juz_bylo[u][v]:
                            G[gdzie_juz_bylo[a][b]].append(warstwa)
                            gdzie_juz_bylo[u][v] = warstwa
                            Q.put((u, v))
                            warstwa += 1
    # dfs lecę po grafie
    result = []
    while r is not None:
        result.append(r)
        r = parent[r]
    result.append((x,y))
    return None


runtests(keep_distance)
