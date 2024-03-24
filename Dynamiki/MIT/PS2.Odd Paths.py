def TS(G):
    visited = [False for _ in range(len(G))]
    result = []
    for idx in range(len(G)):
        if not visited[idx]:
            dfsVisit(G, idx, result, visited)
    result = result[::-1]
    return result


def dfsVisit(G, s, result, visited):
    visited[s] = True

    for el in G[s]:
        if not visited[el]:
            dfsVisit(G, el, result, visited)
    result.append(s)


def Odd_paths(s, t, G):
    topological_sort = TS(G)  # posortowane topologicznie wierzchołki
    idx_s, idx_t = -1, -1
    n = len(G)
    idx = 0
    while idx < n:
        if topological_sort[idx] == s:
            idx_s = idx
        elif topological_sort[idx] == t:
            idx_t = idx
        elif idx_t != -1 and idx_s == -1:
            return False
        elif idx_s != -1 and idx_t != -1:
            break
        idx += 1

    dp = [0 for i in range(n)]  # ile dróg wychodzi z wierzchołków od s do v-1 i wchodzi do i-tego wierzchołka
    dp[topological_sort[idx_s]] = 1
    for i in range(idx_s, idx_t):
        for v in G[topological_sort[i]]:
            dp[v] += dp[topological_sort[i]]

    return dp[topological_sort[idx_t]]


G = [[1],
     [2, 3],
     [4, 5],
     [6],
     [6,7],
     [6],
     [8],
     [8],
     []]
print(Odd_paths(1,8,G))
