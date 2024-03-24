import heapq
from math import inf

def lazy_dijkstras(graph, root,boll,cel):
    n = len(graph)
    # set up "inf" distances
    dist = [inf for _ in range(n)]
    # set up root distance
    dist[root] = 0
    # set up visited node list
    visited = [False for _ in range(n)]
    parent = [False for _ in range(n)]
    # set up priority queue
    pq = [(0, root,boll)]
    # while there are nodes to process
    while len(pq) > 0:
        # get the root, discard current distance
        _, u,b = heapq.heappop(pq)
        # if the node is visited, skip
        if visited[u]:
            continue
        # set the node to visited
        visited[u] = True
        # check the distance and node and distance
        if b:
            for v, l in graph[u]:
                # if the current node's distance + distance to the node we're visiting
                # is less than the distance of the node we're visiting on file
                # replace that distance and push the node we're visiting into the priority queue
                if dist[u] + l < dist[v]:
                    dist[v] = dist[u] + l
                    b = False
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v,b))
        else:
            for v, l in graph[u]:
                # if the current node's distance + distance to the node we're visiting
                # is less than the distance of the node we're visiting on file
                # replace that distance and push the node we're visiting into the priority queue
                if dist[u] < dist[v]:
                    dist[v] = dist[u]
                    b = True
                    parent[v] = u
                    heapq.heappush(pq, (dist[v], v,b))
    return dist[cel],parent

def leniwy_kierwoca(G,start,cel):
    dist_0, parent_0 = lazy_dijkstras(G,start,False,cel)
    dist_1, parent_1 = lazy_dijkstras(G, start, True, cel)
    wynik = [cel]
    i = cel
    if dist_1 < dist_0:
        while i != False:
            wynik.append(parent_1[i])
            i = parent_1[i]
        return "zaczyna Alicja" , wynik
    else:
        while i != False:
            wynik.append(parent_0[i])
            i = parent_0[i]

        return "Zaczyna Bob", wynik



G = [[(1, 4), (2, 1), (3, 5)],
     [(0, 1), (4, 2)],
     [(0, 1), (5, 8), (6, 7)],
     [(0, 5), (5, 7)],
     [(1, 2), (7, 10)],
     [(2, 8), (3, 7), (8, 3)],
     [(2, 7), (7, 6)],
     [(4, 10), (6, 6), (9, 11)],
     [(5, 3), (9, 9)],
     [(7, 11), (8, 9)]]

print(leniwy_kierwoca(G,0,9))