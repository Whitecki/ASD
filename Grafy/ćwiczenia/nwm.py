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


    for u in range(V):
        for v, w in G[u]:
            if v > u:
                E.append((u, v, w))

    E = sorted(E, key=lambda x: x[2])
    for i in range(len(G)):
        A = [None for _ in range(V)]
        for i in range(V):
            A[i] = makeset(i)

        count = 0
        MST = []

        for u, v, w in E:
            if union(A[u], A[v]):
                count += 1
                MST.append((u, v))
            if count == V - 1:
                break

    return MST