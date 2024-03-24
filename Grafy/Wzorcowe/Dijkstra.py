from queue import PriorityQueue
from math import inf

# def Dijkstra(a,G):
#     n = len(G)
#     Q = PriorityQueue()
#     Q.put((0, a))
#     distance_a = [inf for i in range(n)]
#     distance_a[a] = 0
#     while not Q.empty():
#         val, u = Q.get()
#         for el in G[u]:
#             v, w = el
#             if val + w < distance_a[v]:
#                 distance_a[v] = val + w
#                 Q.put((distance_a[v], v))
#
#     return distance_a

#############

from math import inf


def heapify(Heap, Gdzie_w_kopcu, i, n):
    l, r, max_idx = 2 * i + 1, 2 * i + 2, i

    if l < n and Heap[l][0] < Heap[max_idx][0]:
        max_idx = l
    if r < n and Heap[r][0] < Heap[max_idx][0]:
        max_idx = r

    if max_idx != i:
        Heap[i], Heap[max_idx] = Heap[max_idx], Heap[i]
        Gdzie_w_kopcu[Heap[i][1]], Gdzie_w_kopcu[Heap[max_idx][1]] = Gdzie_w_kopcu[Heap[max_idx][1]], Gdzie_w_kopcu[Heap[i][1]]
        heapify(Heap, Gdzie_w_kopcu, max_idx, n)


def heapify_up( Heap, Gdzie_w_kopcu, i):
    max_idx = (i - 1) // 2
    if max_idx > -1 and Heap[i][0] < Heap[max_idx][0]:
        Heap[i], Heap[max_idx] = Heap[max_idx], Heap[i]
        Gdzie_w_kopcu[Heap[i][1]], Gdzie_w_kopcu[Heap[max_idx][1]] = Gdzie_w_kopcu[Heap[max_idx][1]], Gdzie_w_kopcu[Heap[i][1]]
        return heapify_up(Heap,Gdzie_w_kopcu, max_idx)
    return i


def delete(Heap, Gdzie_w_kopcu, L, d):  # usuwam i-ty element
    Heap[d], Heap[L - 1] = Heap[L - 1], Heap[d]
    Heap[L-1] = (inf, Heap[L-1][1])
    Gdzie_w_kopcu[Heap[d][1]], Gdzie_w_kopcu[Heap[L - 1][1]] = Gdzie_w_kopcu[Heap[L - 1][1]], Gdzie_w_kopcu[Heap[d][1]]
    heapify(Heap, Gdzie_w_kopcu, heapify_up(Heap, Gdzie_w_kopcu, d), L)


def insert(val, Heap, Gdzie_w_kopcu, L, i):
    Heap[L - 1] = (val, Heap[L-1][1])
    heapify(Heap, Gdzie_w_kopcu, heapify_up(Heap, Gdzie_w_kopcu,L - 1), L)

def Dijkstra(a,G):
    n = len(G)
    Heap = [(inf, i) for i in range(n)]
    Heap[a],Heap[0] = Heap[0], (0,a)
    Gdzie_w_kopcu = [i for i in range(n)]
    Gdzie_w_kopcu[a], Gdzie_w_kopcu[0] = Gdzie_w_kopcu[0], Gdzie_w_kopcu[a]
    distance_a = [inf for i in range(n)]
    distance_a[a] = 0
    visited = [False for _ in range(n)]
    cnt = 0 # ile wierzchołków przerobiłem
    while cnt < n:
        val, u = Heap[0]
        # trzeba wierzchołek i oznaczyć jako odwiedzony
        delete(Heap, Gdzie_w_kopcu, n, Gdzie_w_kopcu[u])
        insert(inf, Heap, Gdzie_w_kopcu, n, u)
        visited[u] = True
        cnt += 1
        for el in G[u]:
            v, w = el
            if val + w < distance_a[v] and not visited[v] and val+w < Heap[Gdzie_w_kopcu[v]][0]:# musze dodać warunek spr wartość
                distance_a[v] = val + w
                delete(Heap, Gdzie_w_kopcu, n, Gdzie_w_kopcu[v])
                insert(val+w, Heap, Gdzie_w_kopcu, n, v)
                #dodaje wierzchołek

    return distance_a


G = [[(1,1),(2,2)],
     [(0,1),(3,1),(4,3)],
     [(0,2),(3,3)],
     [(1,1),(2,3),(4,1),(5,2)],
     [(1,3),(3,1),(5,4)],
     [(3,2),(4,4),(6,1),(7,4)],
     [(5,1),(7,2),(8,100)],
     [(5,4),(6,2)],
     [(6,100)]]

print(Dijkstra(0,G))