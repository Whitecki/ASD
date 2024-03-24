# Policzyć liczbę spójnych składowych w grafie (implementacja przeciwna do tej z poprzedniego zadania)

# Zadanie 3. (BFS i najkrótsze ścieżki) Proszę zaimplementować algorytm BFS tak, żeby znajdował
# najkrótsze ścieżki w grafie i następnie, żeby dało się wypisać najkrotszą ścieżkę z zadanego punktu startowego
# do wskazanego wierzchołka.

from queue import Queue


def BFS(Graf, start,wynik):
    kolejka = Queue()
    n = len(Graf)
    visited = [False for _ in range(n)]
    visited[start] = True
    wynik[start] = True
    kolejka.put(start)
    m = len(Graf[0])

    while not kolejka.empty():
        wierzchołek = kolejka.get()


        for i in range(m):
            if Graf[wierzchołek][i]:
                verticle = i
                if not visited[verticle]:
                    visited[verticle] = True
                    kolejka.put(verticle)
                    wynik[verticle] = True


def spójny(G):

    licznik = 0
    n = len(G)
    wynik = [False for _ in range(n)]
    for i in range(n):
        if not wynik[i]:
            licznik += 1
            BFS(G,i,wynik)


    return licznik

graph = [[0, 1, 1, 0, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0],
         [1, 0, 0, 1, 0, 0, 0, 0, 0],
         [0, 1, 1, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 0]]
print(spójny(graph))
