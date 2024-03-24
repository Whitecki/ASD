# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
#
# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|,
# where |val| denotes the absolute value of val.
#
# Return the minimum cost to make all points connected.
# All points are connected if there is exactly one simple path between any two points.

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)

    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1
    return True


def makeset(x):
    return Node(x)


def kruskal(G):
    V = len(G)
    E = []
    A = [None for _ in range(V)]

    #sortujemy krawędzie po wagach
    for u in range(V):
        for v, w in G[u]:
            if v > u:
                E.append((u, v, w))

    E = sorted(E, key=lambda x: x[2])

    for i in range(V):
        A[i] = makeset(i)

    #Tworzymy MST jako zbiór pusty
    count = 0
    MST = []

    #przeglądaj krawędzie z E w kolejności nierosnących wag
    for u, v, w in E:
        if union(A[u], A[v]):
            count += 1
            MST.append((u, v))
        if count == V - 1:
            break

    return MST


from math import inf


def minCostConnectPoints(points):
    n = len(points)
    G = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                G[i].append((j, abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])))

    A = kruskal(G)
    suma = 0
    for i,j in A:
        suma += (abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1]))
    return suma
points = [[3,12],[-2,5],[-4,1]]
print(minCostConnectPoints(points))

#działa :)))