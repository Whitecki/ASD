# Zadanie 7. (problem stacji benzynowych na grafie) Pewien podróżnik chce przebyć trasę z punktu A
# do punktu B. Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści
# się dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie wierzchołki to miasta a krawędzie to
# łączące je drogi. Każda krawędź ma długość w kilometrach (przedstawioną jako licza naturalna). W każdym
# wierzchołku jest stacja benzynowa, z daną ceną za litr paliwa. Proszę podać algorytm znajdujący trasę z
# punktu A do punktu B o najmniejszym koszcie. Proszę uzasadnić poprawność algorytmu.

from queue import PriorityQueue
from math import inf

#
# def redański_szpieg(G,start):
#     #robimy kolejke priorytetową
#     kolejka = PriorityQueue()
#     n = len(G)
#     #robimy tablice odległości od startu
#     odległość = [inf for _ in range(n)]
#     #wkładamy graf, z pierwszym elementem, którego odległość to 0
#     kolejka.put((0,start))
#
#     while not kolejka.empty() and n > 0:
#         trip, u = kolejka.get()
#         #robimy relaksacje
#         if trip < odległość[u]:
#             odległość[u] = trip
#             n -= 1
#
#             for krawędzie in G[u]:
#                 v , l = krawędzie
#                 kolejka.put((l + trip,v))
#
#     return odległość


def relax(graph, vertex, source, distance, cost):
    flag = False
    for i in range(distance, len(graph[vertex])):
        for j in range(i - distance, len(graph[vertex])):
            if graph[source][i] + j * cost < graph[vertex][j]:
                graph[vertex][j] = graph[source][i] + j * cost
                flag = True

    if flag:
        return True
    return False


def cheapest_trip_with_refueling(graph, city_a, city_b, capacity):
    #dynamizna tblica 2D
    new_graph = [[inf] * (capacity + 1) for _ in range(len(graph))]
    for i in range(len(new_graph[0])):
        new_graph[0][i] = i * graph[0][1]
    #dijkstra
    queue = PriorityQueue()
    queue.put((0, city_a))
    visited = [False] * len(graph)
    parent = [None] * len(graph)
    while not queue.empty():
        distance, u = queue.get()
        for v in graph[u][0]:
            vertex, dist = v
            if not visited[vertex]:
                if dist <= capacity:
                    if relax(new_graph, vertex, u, dist, graph[vertex][1]):
                        parent[vertex] = u
                        queue.put((new_graph[vertex][dist], vertex))
        visited[u] = True

    #zczytywanie drogi
    tour = []
    while city_b != parent[city_a]:
        tour.append(city_b)
        city_b = parent[city_b]
    tour.reverse()
    return tour


graph = [[[(1, 5), (2, 3)], 8],
         [[(0, 4), (2, 3), (3, 5)], 5],
         [[(0, 3), (1, 3), (3, 4)], 3],
         [[(1, 5), (2, 4), (4, 6)], 2],
         [[(3, 6)], 1]]
city_a = 0
city_b = len(graph) - 1
print(cheapest_trip_with_refueling(graph, city_a, city_b, 6))