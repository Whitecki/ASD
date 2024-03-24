def dfs_euler_cycle(graph):
    # Tworzymy stos i dodajemy do niego dowolny wierzchołek
    stack = [next(iter(graph))]
    # Tworzymy pusty cykl
    cycle = []
    while stack:
        v = stack[-1]
        if len(graph[v]):
            # Dodajemy krawędź do stosu i usuwamy ją z grafu
            u = graph[v].pop()
            stack.append(u)
        else:
            # Usuwamy wierzchołek ze stosu i dodajemy go do cyklu
            stack.pop()
            cycle.append(v)
    # Sprawdzamy, czy graf zawiera cykl Eulera
    if len(cycle) == len(graph)+1:
        # Zwracamy cykl Eulera
        return cycle[::-1]
    else:
        # Graf nie zawiera cyklu Eulera
        return None
G = [[1,2],
     [0,2,3,5],
     [0,1,3,5],
     [1,2,4,5,6,8],
     [3,5],
     [1,2,3,4],
     [3,7],
     [6,8],
     [3,7]]

print(dfs_euler_cycle(G))