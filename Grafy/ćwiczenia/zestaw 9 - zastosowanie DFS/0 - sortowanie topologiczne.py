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

Graf = [[1,2,5],
        [2,4],
        [],
        [],
        [3,6],
        [4],
        []]

print(dfs(Graf))