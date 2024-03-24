# https://leetcode.com/problems/max-area-of-island/

"""
idea: Klasyczne zadanie na dfs. Zrobio=łem strukturą Find-Union, by ją przećwiczyć.
time complexity: O( N + M + log∣Σ∣ )
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def find(u):
            if u == parent[u]:
                return u
            else:
                parent[u] = find(parent[u])
                return parent[u]

        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return
            if size[pv] > size[pu]:
                parent[pu] = pv
                size[pv] += size[pu]
            else:
                parent[pv] = pu
                size[pu] += size[pv]

        m = len(grid)
        n = len(grid[0])
        f = 0
        parent = [i for i in range(m * n)]
        size = [1 for i in range(m * n)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    f = 1
                    a = i * n + j
                    for u, v in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if 0 <= u < m and 0 <= v < n and grid[u][v]:
                            b = u * n + v
                            union(a, b)
        if f == 0:
            return 0
        return max(size)



grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(grid))
