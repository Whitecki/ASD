# Zadanie 2. (dobry początek) Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli
# każdy inny wierzchołek można osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm, który
# stwierdza czy dany graf zawiera dobry początek.
from random import randint
from queue import Queue


def new_start(G):
    To_check = Dfs(G)
    #trzeba sprawdzić czy inny wierzchołek ma krawędź do To_check



    return DFS(G,To_check)



def DFS(G, x):
    global time, visited
    visited = [False for _ in range(len(G))]
    time = 0

    dfsVISIT(G, x)
    for idx in range(len(G)):
        if not visited[idx]:
            return False
    return True

def dfsVISIT(G, s):
    global time, visited
    time += 1
    visited[s] = True

    for el in G[s]:
        if not visited[el]:
            dfsVISIT(G, el)
    time += 1


def Dfs(G):
    global visited ,wynik
    visited = [False for _ in range(len(G))]
    wynik = []
    for idx in range(len(G)):
        if not visited[idx]:
            dfsVisit(G, idx)
    wynik.reverse()
    return wynik[0]

def dfsVisit(G, s):

    global visited, wynik
    a = visited
    b = wynik
    visited[s] = True
    if len(G[s]) == 0:
        wynik.append(s)
    for el in G[s]:
        if not visited[el]:
            dfsVisit(G, el)
        if el == G[s][-1]:
            wynik.append(s)


Graf = [[] for _ in range(20)]

liczby = [i for i in range(20)]
for j in range(20):
    a = randint(0,19)
    for i in range(a):
        b = randint(0, 19-i)
        Graf[j].append(liczby[b])

print(new_start(Graf))
