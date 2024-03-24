# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node
# n - 1 and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed
# edge from node i to node graph[i][j]).

'''idea: W tablicy result umieszczamy posortowany topologicznie graf. Następnie odnajduje numery indeksów pod którymi
znajdują się wierzcołki 0(start) i n-1(end) po posortowaniu. Jeżeli wierzchołek od którego mamy zacząć, jest po
wierzchołku do którego mamy dojśc to zwracamy pustą tablice. Następnie tworzymy tablice pomocniczą is_between, która
odpowiada na pytanie "czy wierzchołek o indeksie idx znajduje się w tablicy result pomiędzy indeksami start i end.
Następnie tworze wszystkie parami różne drogi os start do end za pomoca kolejki.
Time complexity: O(v+e)
Stan buzi: fajne zadanko -> uśmiech :)))
'''


# def dfsVisit(G, s, result, visited):
#     visited[s] = True
#
#     for el in G[s]:
#         if not visited[el]:
#             dfsVisit(G, el, result, visited)
#     result.append(s)
#
#
# def allPathsSourceTarget(G):
#     n = len(G)
#     visited = [False for _ in range(n)]
#     result = []
#     for idx in range(n):
#         if not visited[idx]:
#             dfsVisit(G, idx, result, visited)
#     result = result[::-1]
#     start, end = -1, -1
#     for i in range(n):
#         if result[i] == 0:
#             start = i
#         elif result[i] == n-1:
#             end = i
#     is_between = [False for _ in range(n)]
#     is_between[end], is_between[start] = True , True
#     for i in range(start, end):
#         is_between[result[i]] = True
#     dp = [0 for _ in range(n)]
#     dp[0] = 1
#     for i in range(start,end):
#         for el in G[i]:
#             if is_between[el]:
#                 dp[el-start] += dp[i]
#     return dp[n-1]
#zwracam ile jest ścieżekk :))
from queue import Queue
def dfsVisit(G, s, result, visited):
    visited[s] = True

    for el in G[s]:
        if not visited[el]:
            dfsVisit(G, el, result, visited)
    result.append(s)


def allPathsSourceTarget(G):
    n = len(G)
    visited = [False for _ in range(n)]
    result = []
    for idx in range(n):
        if not visited[idx]:
            dfsVisit(G, idx, result, visited)
    result = result[::-1]
    start, end = -1, -1
    for i in range(n):
        if result[i] == 0:
            start = i
        elif result[i] == n-1:
            end = i
    is_between = [False for _ in range(n)]
    if end < start:
        return
    is_between[end], is_between[start] = True , True
    for i in range(start, end):
        is_between[result[i]] = True
    AllPaths = []
    Q = Queue()
    Q.put(([0],start))
    while not Q.empty():
        ActPth,idx = Q.get()
        flag = True
        for el in G[idx]:
            if flag:
                NewPth = [ActPth[i] for i in range(len(ActPth))]
            if el == result[end]:
                NewPth.append(el)
                AllPaths.append(NewPth)
                flag = True
            elif is_between[el]:
                NewPth.append(el)
                Q.put((NewPth,el))
                flag = True
            else:
                flag = False
    return AllPaths


G =[[2],[],[1]]
print(allPathsSourceTarget(G))
