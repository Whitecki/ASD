# Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie
# wierzchołki w grafie, przez każdy dokładnie raz. W ogólnym grafie znalezienie ścieżki Hamiltona jest problemem NP-trudnym. Proszę podać algorytm, który stwierdzi czy istnieje ścieżka Hamiltona w acyklicznym
# grafie skierowanym.

# sortuje wszystko topologicznie

def dfs(G):
    global visited ,wynik
    visited = [False for _ in range(len(G))]
    wynik = []
    for idx in range(len(G)):
        if not visited[idx]:
            dfsVisit(G, idx)
    wynik.reverse()
    return wynik

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

def Musical(G):

    sprawdzić = dfs(G)
    print(sprawdzić)

    n = len(sprawdzić)

    for i in range(n-1):
        a = sprawdzić[i]
        b = sprawdzić[i+1]
        for j in range(len(G[a])):
            if G[a][j] == b:
                break

        if j == len(G[a]):
            return False
    return True

Graf = [[1],
        [2,3],
        [4],
        [0,4],
        [3],
        [0,3]]

print(Musical(Graf))

