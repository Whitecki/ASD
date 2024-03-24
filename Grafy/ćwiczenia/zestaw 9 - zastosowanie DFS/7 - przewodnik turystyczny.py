from queue import PriorityQueue
from random import randint


def redański_szpieg(G, start, koniec, populacja):

    G = zamiana(G)

    # robimy kolejke priorytetową
    kolejka = PriorityQueue()
    n = len(G)

    # dynamiczne tablice, oznaczające ile osób maksymalnie może się znaleźć w tym wierzchołku (odległość)
    # i idąc z którego wierzchołka(parent) #2*O(V)
    parent = [False for _ in range(n)]
    odległość = [0 for _ in range(n)]

    odległość[0] = populacja
    kolejka.put((populacja, start))

    #O(ElogV)
    while not kolejka.empty():
        trip, u = kolejka.get()

        for krawędzie in G[u]:
            v, ile = krawędzie

            # relaksacja
            if ile <= trip:
                if odległość[v] < ile:
                    parent[v] = u
                    odległość[v] = ile
                    kolejka.put((ile, v))
            else:
                if odległość[v] < trip:
                    parent[v] = u
                    odległość[v] = trip
                    kolejka.put((trip, v))

    # z dynamicznej tablicy parent zczytujemy trase #O(V)
    i = koniec
    trasa = [koniec]
    while i != False:
        trasa.append(parent[i])
        i = parent[i]

    # liczymy na ile gróp trzeba podzielić ludzi #O(1)
    if populacja // odległość[koniec] == populacja / odległość[koniec]:
        ile_grup = populacja // odległość[koniec]
    else:
        ile_grup = (populacja // odległość[koniec]) + 1

    return ile_grup, trasa

def zamiana(G):
    o = len(G)
    m = 0
    #O(E)
    for i in range(o):
        m = max(G[i][0],G[i][1],m)

    #O(V)
    T = [[]for _ in range(m+1)]
    #O(E)
    for krotki in G:
        x,y,waga = krotki
        T[x].append((y,waga))
        T[y].append((x,waga))

    return T



G = [(0, 1, 12), (0, 2, 10), (1, 3, 11), (1, 4, 7), (2, 4, 8), (2, 6, 14),
         (3, 5, 8), (4, 6, 8), (5, 7, 11), (6, 7, 6)]

print(redański_szpieg(G, 0, 7, 80))
