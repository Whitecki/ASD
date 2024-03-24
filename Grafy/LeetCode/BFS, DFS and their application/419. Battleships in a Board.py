# Given an m x n matrix board where each cell is a battleship 'X' or empty '.',
# return the number of the battleships on board.
# Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape
# 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical
# cell separates between two battleships (i.e., there are no adjacent battleships).
'''idea: dfs :00'''


def dfs(G):
    def dfsVisit(G, i, j, visited):
        visited[i][j] = True

        for el in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if -1 < i + el[0] < n and -1 < j + el[1] < m and not visited[i + el[0]][j + el[1]] and G[i][j] == 'X':
                dfsVisit(G, i + el[0], j + el[1], visited)

    n, m = len(G), len(G[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and G[i][j] == 'X':
                result += 1
                dfsVisit(G, i, j, visited)
    return result


G = [["."]]
print(dfs(G))
