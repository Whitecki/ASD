# You are given an integer n denoting the number of nodes of a weighted directed graph. The nodes are numbered from 0
# to n - 1.
#
# You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] denotes that there exists a
# directed edge from fromi to toi with weight weighti.
#
# Lastly, you are given three distinct integers src1, src2, and dest denoting three distinct nodes of the graph.
#
# Return the minimum weight of a subgraph of the graph such that it is possible to reach dest from both src1 and src2
# via a set of edges of this subgraph. In case such a subgraph does not exist, return -1.
#
# A subgraph is a graph whose vertices and edges are subsets of the original graph. The weight of a subgraph is the sum
# of weights of its constituent edges.

"""
Odpalam dijkstre z wierzchołków src1, src2, dest i zwracam 3 tablice dist. O(ElogV)
Rozwiązaniem jest min(dist1[v] + dist2[v] + dist3[v]), obliczone dla każdego wierzchołka. O(V)
"""

from queue import PriorityQueue
from math import inf


def minimumWeight(n, edges, src1, src2, dest):
    lenn = [0 for _ in range(n)]
    # zamieniam na liste sąsiedztwa O(E+V)
    G = [[] for _ in range(n)]
    for x, y, w in edges:
        G[x].append([y, w])
        lenn[x] += 1

    # zamieniam multigraf w zwyczajny graf O()
    for i in range(n):
        G[i] = sorted(G[i], key=lambda x: x[0])
        for j in range(1, lenn[i]):
            if G[i][j][0] == G[i][j-1][0]:
                if G[i][j][1] > G[i][j-1][1]:
                    G[i][j][1] = G[i][j-1][1]
                G[i][j-1] = [-1,-1]
        T = []
        for k in range(lenn[i]):
            if not G[i][k] == [-1,-1]:
                T.append(G[i][k])
            else:
                lenn[i] -= 1
        G[i] = [T[k] for k in range(lenn[i])]
    # tworze graf w którym krawędzie są skierowane w druga strone
    reverse_G = [[] for _ in range(n)]
    for i in range(n):
        for y in range(lenn[i]):
            a = G[i][y]
            x,w = G[i][y]
            reverse_G[x].append([i,w])

    # 3 dijkstry na raz, bo Elog(3*V) jest lepsze od 3Elog(V)
    Q = PriorityQueue()
    Q.put((0, "src1", src1))
    Q.put((0, "src2", src2))
    Q.put((0, "dest", dest))
    distance_src1 = [inf for _ in range(n)]
    distance_src2 = [inf for _ in range(n)]
    distance_dest = [inf for _ in range(n)]
    distance_src1[src1], distance_src2[src2], distance_dest[dest] = 0, 0, 0
    while not Q.empty():
        val, which_one, u = Q.get()
        if which_one == "dest":
            for v, w in reverse_G[u]:
                if val + w < distance_dest[v]:
                    distance_dest[v] = val + w
                    Q.put((distance_dest[v], "dest", v))
        else:
            for v, w in G[u]:
                if which_one == "src1":
                    if val + w < distance_src1[v]:
                        distance_src1[v] = val + w
                        Q.put((distance_src1[v], "src1", v))
                else:
                    if val + w < distance_src2[v]:
                        distance_src2[v] = val + w
                        Q.put((distance_src2[v], "src2", v))

    result = inf
    for i in range(n):
        result = min(distance_src1[i] + distance_src2[i] + distance_dest[i], result)

    return result

n = 5
edges = [[4,2,20],[4,3,46],[0,1,15],[0,1,43],[0,1,32],[3,1,13]]
src1 = 0
src2 = 4
dest = 1

print(minimumWeight(n,edges,src1,src2,dest))