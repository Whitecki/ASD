# Dany jest graf G = (V, E), gdzie każda krawędź ma wagę ze zbioru {1, . . . , ∣E∣} (wagi krawędzi są parami różne).
# Proszę zaproponować algorytm, który dla danych wierzchołków x i y oblicza ścieżkę o najmniejszej sumie wag, która
# prowadzi z x do y po krawędziach o malejących wagach (jeśli ścieżki nie ma to zwracamy ∞).

'''
idea:
złożoność:
'''

from queue import PriorityQueue
from math import inf

def Dijkstra(a,b,G):
    n = len(G)
    Q = PriorityQueue()
    Q.put((0, a,None))
    visited = [(inf,0) for _ in range(n)]
    visited[a] = ()
    while not Q.empty():
        val, u, last_waga = Q.get()
        #Jeśli dotarłem do końca to uaktualniam minimalny koszt dotarcia
        if u == b:
            return val


        for el in G[u]:
            v, w = el
            if (visited[v][0] > val + w or visited[v][1] < w) and last_waga > w:
                #aktualizuje

                visited[v] = True
                Q.put((val+w, v, w))

    return inf


#nie działa kurwa