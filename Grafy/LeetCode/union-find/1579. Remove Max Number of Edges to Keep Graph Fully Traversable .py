class Node:
    def __init__(self):
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


def maxNumEdgesToRemove(n, edges):
    Ala = [Node() for _ in range(n+1)]
    Bob = [Node() for _ in range(n+1)]
    cnt, cnta, cntb = 0, 0, 0
    for typ, x, y in edges:
        if typ == 3:
            # najpierw niebieskie dajemy, więc wystarczy sprawdzić tylko jedno z nich
            if find(Ala[x]) != find(Ala[y]):
                union(Ala[x], Ala[y])
                union(Bob[x], Bob[y])
                cnt += 1

    for typ, x, y in edges:
        if find(Ala[x]) != find(Ala[y]) and typ == 1:
            union(Ala[x], Ala[y])
            cnta += 1
        if find(Bob[x]) != find(Bob[y]) and typ == 2:
            union(Bob[x], Bob[y])
            cntb += 1
    if cnt + cnta < n-1 or cnt + cntb < n-1:
        return -1
    if cnta == cntb and cnt + cnta == n-1:
        return len(edges) - (cnt + cnta + cntb)
    return -1

n = 4
edges = [[3,2,3],[1,1,2],[2,3,4]]
print(maxNumEdgesToRemove(n,edges))

# trzeba dodać przypadek gdy nie da sie zbudować drzewa