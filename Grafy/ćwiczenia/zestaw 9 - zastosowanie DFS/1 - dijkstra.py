# . Proszę zaimplementować algorytm Dijkstry (dla wybranej przez prowadzącego reprezentacji grafu)

from queue import PriorityQueue
from math import inf

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

def Dijkstra(G, s):
    kolejka = PriorityQueue()
    trip = 0
    n = len(G)
    odległości = [inf for _ in range(n)]
    odległości[s] = 0
    kolejka.put((trip, s))

    while not kolejka.empty():

        trip, v = kolejka.get()

        for u in G[v]:
            wierzchołek, waga = u
            if trip + waga < odległości[wierzchołek]:
                odległości[wierzchołek] = trip + waga
                kolejka.put((trip + waga, wierzchołek))
    return odległości,n

graph = [[(1,12),(2,10)],
         [(0,12),(3,11),(4,7)],
         [(0,10),(4,8),(6,14)],
         [(1,11),(5,8)],
         [(1,7),(2,8),(6,8)],
         [(3,8),(7,11)],
         [(2,14),(4,8),(7,6)],
         [(5,11),(6,6)]]

# print(redański_szpieg(graph,0))
print(Dijkstra(graph,0))
