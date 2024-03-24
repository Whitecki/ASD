# Pewien podróżnik chce przebyć trasę z punktu A do punktu B. Niestety jego samochód spala dokładnie jeden litr paliwa na
# jeden kilometr trasy. W baku mieścicsię dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie
# wierzchołki to miasta a krawędzie to łączące je drogi. Każda krawędź ma długość w kilometrach (przedstawioną jako licza
# naturalna). W każdym wierzchołku jest stacja benzynowa, z daną ceną za litr paliwa. Proszę podać algorytm znajdujący
# trasę z punktu A do punktu B o najmniejszym koszcie. Proszę uzasadnić poprawność algorytmu.

from queue import PriorityQueue
from math import inf

def Dijkstra(a,b,D,G):
    n = len(G)
    Q = PriorityQueue()
    Q.put((0, a))
    distance_a = [[inf for _ in range(D+1)] for _ in range(n)]
    distance_a[a][D] = 0
    while not Q.empty():
        val, u, ip = Q.get()
        # tankowanie
        

        for el in G[u]:
            v, w = el
            if val + w < distance_a[v][] and :
                distance_a[v] = val + w
                Q.put((distance_a[v], v))

    return distance_a

