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


def numberOfGoodPaths(vals, edges):
    n = 0
    for x,y in edges:  #O(E)
        n = max(n,x,y)
    #tworze listę sąsiedztwa
    G = [[] for _ in range(n+1)]
    for x,y in edges:
        G[x].append(y)
        G[y].append(x)
    wskaźniki_na_wierzchołki = [Node(i) for i in range(n+1)] #O(V)
    vals = [(vals[i],i) for i in range(n+1)] #O(V)
    wartosci = sorted(vals, key=lambda x: x[0]) #O(VlogV)
    i,counter = 0,0
    while i < n:
        # patrzę które elementy są do dodania
        j = i + 1
        while j < n and wartosci[i][0] == wartosci[j][0]:
            j+=1
        # łącze nowe
        for idx in range(i,j):
            for v in G[idx]:
                if not vals[v] > vals[i]:
                    union(wskaźniki_na_wierzchołki[v],wskaźniki_na_wierzchołki[i])
        cnt = 0
        #zliczam ile powstało nowych googpaths
        for idx in range(i,j):
            pass

        counter += cnt
        i = j


    return n + counter

