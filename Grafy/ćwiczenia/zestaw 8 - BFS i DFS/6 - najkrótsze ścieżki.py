# Zadanie 3. (BFS i najkrótsze ścieżki) Proszę zaimplementować algorytm BFS tak, żeby znajdował
# najkrótsze ścieżki w grafie i następnie, żeby dało się wypisać najkrotszą ścieżkę z zadanego punktu startowego
# do wskazanego wierzchołka.

from queue import Queue

def BFS(Graf, start, koniec):

    kolejka = Queue()
    n = len(Graf)
    visited = [False for _ in range(n)]
    visited[start] = True
    wynik = [False for _ in range(n)]
    kolejka.put(start)

    while not kolejka.empty():
        wierzchołek = kolejka.get()

        for verticle in Graf[wierzchołek]:

            if not visited[verticle]:

                visited[verticle] = True
                kolejka.put(verticle)
                wynik[verticle] = wierzchołek

    result = [koniec]
    while True:

        result.append(wynik[koniec])
        koniec = wynik[koniec]
        if wynik[koniec] == False:
            result.append(wynik[koniec])
            return result





    return wynik


graph = [[1, 2], [0, 3, 4], [0, 6, 7, 8], [1, 5], [1], [3], [2], [2], [9, 10], [8], [8]]
print(BFS(graph, 0,10))






