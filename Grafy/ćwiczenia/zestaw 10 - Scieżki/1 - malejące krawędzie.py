# Dany jest graf G = (V, E), gdzie każda krawędź ma wagę
# ze zbioru {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm, który dla danych
# wierzchołków x i y oblicza ścieżkę o najmniejszej sumie wag, która prowadzi z x do y po krawędziach o
# malejących wagach (jeśli ścieżki nie ma to zwracamy ∞).

from queue import PriorityQueue
from math import inf


def not_stonks(Graf, start, end):
    n = len(Graf)
    o = 0
    for i in range(n):
        o += len(Graf[i])
    where_is_it = [-1 for i in range(o + 1)]
    for i in range(n):
        Graf[i].sort(key=lambda x: x[1], reverse=True)
        for j in range(len(Graf[i])):
            where_is_it[Graf[i][j][1]] = (i, j)

    # klasyczny dijkstra
    queue = PriorityQueue()
    best_distance = inf
    for i in range(len(Graf[start])):
        queue.put((Graf[start][i][1], Graf[start][i][1], Graf[start][i][0]))

    while not queue.empty():
        dist, weight, u = queue.get()
        #sprawdzam czy jestem na końcu
        if u == end:
            best_distance = min(dist, best_distance)
        #sprawdzam czy da się jeszcze osiągnąc lepszą drogę
        if best_distance < dist:
            return best_distance
        #sprawdzam, tylko krawędzie o niższej wadze
        for i in range(weight - 1, 0, -1):
            x, y = where_is_it[i]
            if x == u or Graf[x][y][0] == u:
                # x i u to ten sam wierzchołek, więc po przejściu przez krawędź jestesmy na u
                if x == u:
                    queue.put((Graf[x][y][1] + dist, Graf[x][y][1], Graf[x][y][0]))
                # Graf[x][y][0] i u są tym samym wierzchołkiem, więc przechodzimy na x
                else:
                    queue.put((dist + Graf[x][y][1], Graf[x][y][1], x))
    return best_distance


graph = [[(1, 14), (2, 2), (3, 9)],
         [(2, 13), (4, 7)],
         [(5, 11), (6, 4)],
         [(7, 15), (6, 6)],
         [(8, 10)],
         [(9, 3)],
         [(8, 5)],
         [(9, 8)],
         [(10, 12)],
         [(10, 1)]]

s = 0
t = 10
print(not_stonks(graph, s, t))
