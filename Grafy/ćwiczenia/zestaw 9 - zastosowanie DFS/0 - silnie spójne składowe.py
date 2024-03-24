
def dfs(G):
    global time, visited, kolejność
    n = len(G)
    koljeność = [False for _ in range(n)]
    visited = [False for _ in range(len(G))]
    time = 0

    #spamiętuje kolejność przetworzenia
    for idx in range(len(G)):
        if not visited[idx]:
            odcinamy(G, idx)
    #zamieniam kierunek krawędzi
    T = [[] for _ in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            T[G[j]].append(i)


    # wykonuje DFS w koljenośći czasów przetworzenia

    for i in range(n):
        kolejność[i] = (kolejność[i], i)

    kolejność = sorted(kolejność, key=lambda x: x[0], reverse=True)

    for i in range(n):
        kolejność[i] = kolejność[i][1]

    for idx in kolejność:
        if visited[idx]:
            odcinamy(G, idx)






def dfsVisit(G, s):
    print(s)
    global time, visited, kolejność
    time += 1
    visited[s] = True

    for el in G[s]:
        if not visited[el]:
            odcinamy(G, el)

    time += 1
    kolejność[s] = time


def odcinamy(G, s):

    global visited

    visited[s] = False

    for el in G[s]:
        if visited[el]:
            odcinamy(G, el)

    del
