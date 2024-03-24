# Proszę zaimplementować wybrany przez siebie algorytm obliczania minimalnego drzewa rozpinającego dla wybranej
# przez prowadzącego reprezentacji grafu.

# algorytm Kruskala

# posortuj krawędzie po wagach

class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

# stwórz zbiór A


# przeglądaj krawedzie w koljeności niemalejących wag
# jeśli A u e nie tworzy cyklu to dodaj
def convert_to_edges(graph):
    pass

def rób_Node(i):
    return Node(i)

def MST_by_Kruskal(graf):
    # przy danej reprezentacji grafu, zrób listę krawędzi i ich wierzchołków w formacie (i, j, graph[i][j])
    edges = convert_to_edges(graf)
    # posortuj krawędzie po wagach
    edges.sort(key=lambda x: x[2])
    #stwórz zbiór A
    MST = []
    # lista tablice przechowywującą wszystkie zbiory rozłączne
    V = []
    # robimy z każdej krawędzi zbioru rozłącznego
    for i in range(len(graf)):
        V.append(rób_Node())

    # staramy się połączyć ile się da wierzchołków
    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        if find(V[u]) != find(V[v]):
            MST.append(edges[i])
            union(V[u], V[v])
    return MST



#Zwróć A
