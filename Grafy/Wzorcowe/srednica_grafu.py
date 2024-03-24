"""
generalnie puszczamy bfs z kazdego wierzcholka i szukamy max min odleglosci miedzy dwoma wierzcholkami
dla gestych mozna floyda warshalla - krotsza implementacja, a zlozonosc taka sama
"""
from queue import Queue


def if_const(G):
    # dla listy sasiedztwa
    for i in range(len(G)):
        if not len(G[i]):
            return False
    return True


def srednica(G):

    def bfs(s):
        nonlocal G, d
        visited = [False for _ in range(n)]
        visited[s] = True
        d[s] = 0
        q = Queue()
        q.put(s)
        while not q.empty():
            u = q.get()
            for v in G[u]:
                if not visited[v]:
                    d[v] = d[u] + 1
                    q.put(v)
            visited[u] = True

    if not if_const(G):
        return float("inf")

    n = len(G)
    # parent
    d = [0 for _ in range(n)]
    road = 0
    for i in range(n):
        bfs(i)
        road = max(d)
    return road


G = [[1, 5],
     [0, 2],
     [1, 3],
     [2, 4],
     [3, 5],
     [0, 4]]
print(srednica(G))
