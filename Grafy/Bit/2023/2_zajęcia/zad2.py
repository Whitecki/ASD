"""
Dijkstra na rozmnożonych wierzchołkach
Time: DElogV
"""
from queue import PriorityQueue
from math import inf

def jazda(G:'lista sąsiedztwa',Price:"cena paliwa w każdym mieście",A:'początek ściażki',B:'koniec ścieżki',d:'pojemność baku'):
    n = len(G)
    d = 100
    Q = PriorityQueue()
    distance = [[inf for _ in range(d+1)] for _ in range(n)] #cena dojazdu do tego miejsca z A
    Q.put((0,A,0))
    while not Q.empty():
        (hajs, u, paliwo) = Q.get()
        if distance[u][paliwo] > hajs: # równoważne warunkowi visited
            # tankowanie, robimy to tylko raz
            #for i in range(paliwo + 1, d + 1): zrobiłoby nam na kopcu d*V elementów :((
            if paliwo < d:
                Q.put((hajs + Price[u], u, paliwo + 1))
            for v,w in G[u]:
                if paliwo >= w and distance[v][paliwo - w] > hajs:
                    Q.put((hajs,v,paliwo - w))
            distance[u][paliwo] = hajs
    result = inf
    for el in distance[B]:
        result = min(result,el)
    return result

G = [[[2,40]],
     [[2,100],[3,60]],
     [[0,40],[1,100],[3,80]],
     [[1,60],[2,80]]]

Price = [3,2,5,10]
print(jazda(G,Price,0,1,100))