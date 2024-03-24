# wszystkie krawędzie, odwiedzamy dokładnie raz

# spójny graf nieskierowany ma cykl ojlera, gdy każdy jego wierzchołek ma stopień parzysty

def Euler(G,idx):
    global wynik
    wynik = []
    n = len(G)
    #sortujemy by móc użyc binary search
    for i in range(n):
        G[i] = sorted(G[i])
    # sprawdzamy, czy została jakaś krawędź
    dfsVisit(G, idx)
    return wynik

def binary_search(T, i, j, x):
    if i > j:
        return False
    c = (i + j) // 2
    if T[c] == x:
        return c
    if T[c] > x:
        return binary_search(T, i, c - 1, x)
    else:
        return binary_search(T, c + 1, j, x)

def dfsVisit(G, s):
    global wynik
    while 0 != len(G[s]):
        el = G[s][0]
        # usuwamy krawędzie po których przeszliśmy
        m = len(G[el])
        delete = binary_search(G[el],0,m-1,s)
        del G[s][0]
        del G[el][delete]
        #idziemy do następnego
        dfsVisit(G, el)
    else:
        # jak zostanie przetworzony dany wierzchołek to go zapisujemy
        wynik.append(s)


Graf = [[1,2],
        [0,2,3,5],
        [0,1,3,5],
        [1,2,4,5],
        [3,5],
        [1,2,3,4]]

print(Euler(Graf,0))