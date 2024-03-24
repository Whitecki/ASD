def numIslands(G):
    I = len(G)
    J = len(G[0])
    def dfsVisit(G, i, j, result, visited, I,J):
        visited[i][j] = True
        flag = True
        summ = 0
        for el in [(1, 0), (-1, 0), (0, 1), (0, -1),(1,1),(-1,1),(-1,-1),(1,-1)]:
            if -1 < i + el[0] < I and -1 < j + el[1] < J and not visited[i + el[0]][j + el[1]] and G[i + el[0]][j + el[1]]:
                flag = False
                summ += dfsVisit(G, i + el[0], j + el[1], result, visited, I,J)
        if flag:
            return 1
        return summ + 1
    visited = [[False for _ in range(J)] for _ in range(I)]
    result = 0
    for i in range(I):
        for j in range(J):
            if not visited[i][j] and G[i][j]:
                dfsVisit(G, i, j, result, visited, I,J)
                result += 1
    return result

G = [[0,1],
     [1,0],
     [1,1],
     [1,0]]
print(numIslands(G))