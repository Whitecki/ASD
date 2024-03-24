# Sprawdzanie czy graf jest dwudzielny (czyli zauważyć, że to 2-kolorowanie i użyć DFS lub BFS).


from queue import Queue


def BFS(Graf, start):
    kolejka = Queue()
    n = len(Graf)
    visited = [False for _ in range(n)]
    visited[start] = True
    kolor = [-1 for _ in range(n)]
    kolor[start] = 1
    kolejka.put(start)

    while not kolejka.empty():
        wierzchołek = kolejka.get()

        for verticle in Graf[wierzchołek]:

            if visited[verticle] and kolor[verticle] == kolor[wierzchołek]:
                return False

            if not visited[verticle]:
                visited[verticle] = True
                kolejka.put(verticle)
                if kolor[wierzchołek]:
                    kolor[verticle] = 0

                else:
                    kolor[verticle] = 1





    return True


graph = [[1, 2,6,10], [0, 3, 4], [0, 7, 8], [1, 5], [1], [3], [0], [2], [9, 10], [8], [0,8]]
print(BFS(graph, 0))