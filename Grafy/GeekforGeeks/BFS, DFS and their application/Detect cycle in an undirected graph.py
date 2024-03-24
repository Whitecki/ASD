def is_cyclic(G):
    def dfsVisit(G, s, parent, visited):
        visited[s] = True

        for i in range(len(G[s])):
            if not visited[G[s][i]]:
                if dfsVisit(G, G[s][i], s, visited):
                    return True
            elif parent != s and parent != -1 and G[s][i] != parent:
                return True
        return False
    visited = [False for _ in range(len(G))]
    for i in range(len(G)):
        if not visited[i]:
            if dfsVisit(G, i,-1,visited):
                return 1
    return 0



G = [[1],[0,2,4],[1,3],[2,4],[1,3]]
print(is_cyclic(G))

