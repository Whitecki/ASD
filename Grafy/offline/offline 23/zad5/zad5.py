from zad5testy import runtests
from queue import PriorityQueue
from math import inf

def spacetravel( n, E, S, a, b ):
    #transformacja listy krawędzi do listy sąsiedztwa O(E)
    G = [[] for _ in range(n)]
    for el in E:
        G[el[0]].append([el[1], el[2]])
        G[el[1]].append([el[0], el[2]])

    #dijkstra, szukam najkrótszej drogi z a do wszytskich innych wierzchołków, bez używania portali
    Q = PriorityQueue()
    Q.put((0,a))
    distance_a = [inf for i in range(n)]
    distance_a[a] = 0
    while not Q.empty():
        val,u = Q.get()
        for el in G[u]:
            v,w = el
            if val + w < distance_a[v]:
                distance_a[v] = val + w
                Q.put((distance_a[v],v))

    #szukam najkrótszej drogi z b do wszytskich innych wierzchołków
    Q = PriorityQueue()
    Q.put((0,b))
    distance_b = [inf for i in range(n)]
    distance_b[b] = 0
    while not Q.empty():
        val,u = Q.get()
        for el in G[u]:
            v,w = el
            if val + w < distance_b[v]:
                distance_b[v] = val + w
                Q.put((distance_b[v],v))

    # obliczam odległość (od a do najbliższego portalu + od b do najbliższego portalu) O(V)
    from_a_to_portal, from_b_to_portal = inf,inf
    for el in S:
        if from_a_to_portal > distance_a[el]:
            from_a_to_portal = distance_a[el]
        elif from_b_to_portal > distance_b[el]:
            from_b_to_portal = distance_b[el]

    the_shortest_path = min(distance_a[b],from_b_to_portal+from_a_to_portal)
    if the_shortest_path is not inf:
        return the_shortest_path
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )