# Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to miasta a krawędzie to drogi łączące miasta. Dla
# każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba naturalna). Alicja i Bob prowadzą (na zmianę)
# autobus z miasta x ∈ V do miasta y ∈ V , zamieniając się za kierownicą w każdym kolejnym mieście. Alicja wybiera
# trasę oraz decyduje, kto prowadzi pierwszy. Proszę zaproponować algorytm, który wskazuje taką
# (oraz osobę, która ma prowadzić pierwsza), żeby Alicja przejechała jak najmniej kilometrów. Algorytm powinien być jak
# najszybszy (ale przede wszystkim poprawny).

"""
Pomysł: Rozmnażam wierzchołki, by rozróżnić, kiedy Alicja, a kiedy Bob przyjedzie do danego miasta.
Złożoność: ElogV ?
"""

from queue import PriorityQueue
from math import inf


def leniwa_ala(a, b, G,n):

    Q = PriorityQueue()
    Q.put((0, a, 1,None))
    Q.put((0, a, 0,None))
    distance_ala = [inf for _ in range(n+1)]
    parent_ala = [-1 for _ in range(n+1)]
    distance_bob = [inf for _ in range(n+1)]
    parent_bob = [-1 for _ in range(n+1)]
    distance_ala[a], distance_bob[a] = 0, 0
    parent_ala[a], parent_bob[a] = None, None
    while not Q.empty():
        val, u, czy_ala, parent = Q.get()
        if czy_ala:
            for el in G[u]:
                v, w = el
                if val < distance_ala[v]:
                    parent_ala[v] = u
                    distance_ala[v] = val
                    Q.put((distance_ala[v], v, 0,u))
        else:
            for el in G[u]:
                v, w = el
                if val + w < distance_bob[v]:
                    parent_bob[v] = u
                    distance_bob[v] = val + w
                    Q.put((distance_bob[v], v, 1,u))

    if distance_ala[b] < distance_bob[b]:
        return parent_ala, "bob"
    return parent_bob, "ala"


def f(E,a,b):

    n = 0
    for x, y, c in E:
        n = max(x, y, n)
    G = [[] for _ in range(n + 1)]

    for x, y, c in E:
        G[x].append([y, c])
        G[y].append([x, c])

    parent, first = leniwa_ala(a,b,G,n)
    result = [b]
    i = b
    while i != a:
        result.append(parent[i])
        i = parent[i]
    result = result[::-1]
    return result, first

E = [(0, 1, 8), (0, 2, 15), (0, 5, 12), (0, 10, 10), (0, 12, 30), (1, 4, 15), (1, 2, 4), (2, 3, 7), (3, 1, 10),
     (3, 4, 13), (4, 7, 14), (5, 6, 20), (5, 3, 18), (6, 4, 11), (6, 7, 8), (8, 7, 4), (9, 8, 12), (10, 5, 19),
     (10, 11, 25), (10, 7, 10), (11, 9, 60), (12, 11, 32), (9, 10, 25)]

print(f(E,0,8))
