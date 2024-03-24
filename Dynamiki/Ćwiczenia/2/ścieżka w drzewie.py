from queue import Queue


def smieszna_nazwa(G, root, val):
    n = len(G)
    Q = Queue()
    Q.put((root, root))
    Topological_order = [-1 for _ in range(n)]
    Topological_order[0] = root
    idx = 1
    height = [0 for _ in range(n)]
    while not Q.empty():
        u, p = Q.get()
        for v in G[u]:
            if v != p:
                height[v] = height[u] + 1
                Q.put((v, u))
                Topological_order[idx] = v
                idx += 1
    # największa wartość zaczynająca się na wierzchołku v i idąca w dół
    dp = [0 for _ in range(n)]
    # największa wartość jeśli wierzchołek v jest rootem najbardziej wartościowej ścieżki
    DP = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        the_biggest, the_second = 0, 0
        for v in G[Topological_order[i]]:
            if height[v] > height[Topological_order[i]]:
                if dp[v] > the_biggest:
                    the_biggest, the_second = dp[v], the_biggest
                elif val[v] > the_second:
                    the_second = dp[v]
        DP[Topological_order[i]] = the_biggest + the_second + val[Topological_order[i]]
        dp[Topological_order[i]] = max(max(the_biggest, the_second) + val[Topological_order[i]],
                                       val[Topological_order[i]], 0)
    return max(max(dp),max(DP))


G = [[15],
     [2, 5, 6, 7],  # 1
     [1, 3, 4],
     [2],
     [2],  # 4
     [1, 13],
     [1],
     [1, 8, 9, 14, 15],
     [7],  # 8
     [7],
     [13],
     [13],
     [13],  # 12
     [5, 10, 11, 12],
     [7],
     [0, 7]]

val = [100, 20, 5, 30, -20, -20, 15, -10, 15, 18, -15, 22, 30, 2, 23, -20]

print(smieszna_nazwa(G,1,val))