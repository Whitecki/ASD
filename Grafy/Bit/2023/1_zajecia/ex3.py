# a
def dfs(G):
    n = len(G)
    visited = [[False for _ in range(n)] for _ in range(n)]
    result = 0
    bigger = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and G[i][j]:
                result += 1
                bigger = max(dfsVisit(G, i, j, result, visited, n), bigger)
    return result, bigger


def dfsVisit(G, i, j, result, visited, n):
    visited[i][j] = True
    flag = True
    summ = 0
    for el in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if -1 < i + el[0] < n and -1 < j + el[1] < n and not visited[i + el[0]][j + el[1]] and G[i + el[0]][j + el[1]]:
            flag = False
            summ += dfsVisit(G, i + el[0], j + el[1], result, visited, n)
    if flag:
        return 1
    return summ + 1


def from_edge_to_edge(G):
    n = len(G)
    visited = [[False for _ in range(n)] for _ in range(n)]

    def DFS_visit(G, visited, i, j):
        visited[i][j] = True
        for el in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if -1 < i + el[0] < n and -1 < j + el[1] < n and not G[i + el[0]][j + el[1]] and not visited[i + el[0]][
                j + el[1]]:
                DFS_visit(G, visited, i + el[0], j + el[1])

    DFS_visit(G, visited, 0, 0)
    if visited[n - 1][n - 1]:
        return True
    return False
# d

from queue import PriorityQueue
from math import inf


def dijkstra(G):
    Q = PriorityQueue()
    n = len(G)
    visited = [[inf for _ in range(n)] for _ in range(n)]
    visited[0][0] = 0
    Q.put((0, 0, 0))
    while not Q.empty():
        cnt, i, j = Q.get()
        if cnt + 1 > visited[n-1][n-1]:
            break
        for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if -1 < i + y < n and -1 < j + x < n and cnt + 1 < visited[i + y][j + x] and not G[i+y][j+x]:
                visited[i+y][j+x] = cnt +1
                Q.put((cnt + 1, i + y, j + x))
    if visited[n-1][n-1] == inf:
        return False
    i,j = n-1, n-1
    result = []
    while (i,j) != (0,0):
        for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if visited[i][j] == visited[i-y][j-x] + 1:
                result.append((i,j))
                i,j = i-y,j-x
                break
    result.append((0,0))
    result = result[::-1]
    return result

G = [[0, 1, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 1, 1, 0, 0, 0],
     [0, 0, 0, 1, 1, 0, 1, 0],
     [0, 1, 1, 1, 1, 0, 1, 0],
     [0, 0, 1, 1, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 1, 1],
     [1, 1, 0, 1, 1, 0, 1, 0],
     [0, 0, 0, 1, 0, 0, 0, 0]]

a = dfs(G)
print(a)

boll = from_edge_to_edge(G)
print(boll)

print(dijkstra(G))