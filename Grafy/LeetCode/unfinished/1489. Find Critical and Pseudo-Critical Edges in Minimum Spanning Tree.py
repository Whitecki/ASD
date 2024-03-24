# Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where
# edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning
# tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible
# total edge weight.
#
# Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose
# deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand,
# a pseudo-critical edge is that which can appear in some MSTs but not all.
#
# Note that you can return the indices of the edges in any order.
from queue import PriorityQueue



def Prima(G):
    V = len(G)
    DQ = PriorityQueue()
    W = [float('inf') for _ in range(V)]
    visited = [False for _ in range(V)]
    parent = [None for _ in range(V)]

    W[0] = 0
    DQ.put((W[0], 0))

    while not DQ.empty():

        _, u = DQ.get()

        if not visited[u]:

            visited[u] = True

            for v, w in G[u]:
                if W[v] > w and parent[u] != v:
                    parent[v] = u
                    W[v] = w
                    DQ.put((W[v], v))

    MST = []

    for u in range(1, V):
        MST.append((parent[u], u))

    return MST
