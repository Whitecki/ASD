def SCC(graph):
    visited = [False] * len(graph)
    stack = []
    for i in range(len(graph)):
        if not visited[i]:
            DFSUtil(graph, i, visited, stack)
    new_graph = [[] for _ in range(len(graph))]
    transpose_graph(graph, new_graph)
    for j in range(len(visited)):
        visited[j] = False
    result = [[] for _ in range(len(graph))]
    index = 0
    while len(stack):
        u = stack.pop()
        if not visited[u]:
            dfs(new_graph, u, visited, result, index)
            index += 1
    return result


def dfs(graph, source, visited, result, index):
    visited[source] = True
    result[index].append(source)
    for v in graph[source]:
        if not visited[v]:
            dfs(graph, v, visited, result, index)


def DFSUtil(graph, source, visited, stack):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            DFSUtil(graph, v, visited, stack)
    stack.append(source)


def transpose_graph(graph, new_graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            new_graph[graph[i][j]].append(i)


Graf = [[7],
        [6],
        [1, 3],
        [4, 5],  # 3
        [0],
        [2, 4],
        [],
        [6, 9],  # 7
        [1],
        [5, 8],
        [2]]
print(SCC(Graf))


# robimy SCC

# usuwam z grafu krawędzi wewnętrzne silnie spójnych składowych
# spr czy cały graf nie jest spójną składową !!!!!

def usuwańsko(Graf):
    global istniejące_wierzchołki, T
    T = Graf
    delete = SCC(T)
    m = len(Graf)
    i = 0

    istniejące_wierzchołki = [True for i in range(m + 1)]
    boll = [True for i in range(m + 1)]
    while len(delete[i]) != 0:
        n = len(delete[i])
        a = delete[i][0]
        istniejące_wierzchołki[a] = False
        if n > 1:
            boll[a] = False
            for j in range(1, n):
                Graf[a] += Graf[delete[i][j]]
                Graf[delete[i][j]] = []
                boll[delete[i][j]] = False
            Graf[a] = sorted(set(Graf[a]))
            lista = []
            for k in range(len(Graf[a])):
                if boll[Graf[a][k]]:
                    lista.append(Graf[a][k])
                    istniejące_wierzchołki[Graf[a][k]] = False
                else:
                    boll[Graf[a][k]] = True

            Graf[a] = lista

        i += 1


usuwańsko(Graf)
print(Graf)


# następnie sotrujemy topologicznie

def dfs(graph, source, visited, result):
    visited[source] = True
    for v in graph[source]:
        if not visited[v]:
            dfs(graph, v, visited, result)
    result.insert(0, source)


def topological_sort(graph):
    result = []
    for i in range(len(graph)):
        if not istniejące_wierzchołki[i]:
            dfs(graph, i, istniejące_wierzchołki, result)
    return result


print(T)
print(topological_sort(Graf))
