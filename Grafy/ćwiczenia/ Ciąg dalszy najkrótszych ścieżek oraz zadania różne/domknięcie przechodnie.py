# Proszę zaimplementować algorytm obliczający domknięcie przechodnie grafu reprezentowanego w postaci macierzowej
# (domknięcie przechodnie grafu G, to graf nad tym samym zbiorem wierzchołków, który dla każdych dwóch wierzchołków u i v
# ma krawędź z u do v wtedy i tylko wtedy, gdy w G istnieje ścieżka z u do v.

def floyd_marshall(G):
    V = len(G)
    D = [[float('inf') for i in range(V)] for i in range(V)]
    parent = [[None for i in range(V)] for i in range(V)]

    for u in range(V):
        for v in range(V):
            if u == v:
                D[u][v] = 0
            elif G[u][v] != 0:
                D[u][v] = G[u][v]
                parent[u][v] = u

    for i in range(V):
        for u in range(V):
            for v in range(V):
                if D[u][v] > D[u][i] + D[i][v]:
                    D[u][v] = D[u][i] + D[i][v]
                    parent[u][v] = parent[i][v]

    for i in range(V):
        for j in range(V):
            if D[i][j] == float("inf") or D[i][j] == 0:
                D[i][j] = 0
            else:
                D[i][j] = 1
    return D

graph = [[0, 1, 0, 1, 0],
         [0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0],
         [0, 0, 1, 0, 1],
         [0, 0, 1, 0, 0]]

print(floyd_marshall(graph))