class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)

    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1
    return True


def swimInWater(grid):
    n = len(grid)

    grid_sorted = [-1 for _ in range(n ** 2)]
    for i in range(n):
        for j in range(n):
            grid_sorted[grid[i][j]] = (i, j)
    A = [[Node(grid[i][j]) for j in range(n)] for i in range(n)]
    value = 0
    while find(A[0][0]) != find(A[n - 1][n - 1]):
        # Sprawdzam, czy któryś dookoła mogę wziąć, jeśli tak to biorę i powtarzam zabawę.
        def f(cnt):
            if cnt[0] + 1 < n and A[cnt[0] + 1][cnt[1]].value < value and find(A[cnt[0] + 1][cnt[1]]) != find(
                    A[cnt[0]][cnt[1]]):
                union(A[cnt[0] + 1][cnt[1]], A[cnt[0]][cnt[1]])
                f((cnt[0]+1,cnt[1]))
            if cnt[1] + 1 < n and A[cnt[0]][cnt[1]+1].value < value and find(A[cnt[0]][cnt[1]+1]) != find(
                    A[cnt[0]][cnt[1]]):
                union(A[cnt[0]][cnt[1]+1], A[cnt[0]][cnt[1]])
                f((cnt[0], cnt[1]+1))
            if cnt[0] > 0 and A[cnt[0] - 1][cnt[1]].value < value and find(A[cnt[0] - 1][cnt[1]]) != find(
                    A[cnt[0]][cnt[1]]):
                union(A[cnt[0] - 1][cnt[1]], A[cnt[0]][cnt[1]])
                f((cnt[0] - 1, cnt[1]))
            if cnt[1] > 0 and A[cnt[0]][cnt[1] - 1].value < value and find(A[cnt[0]][cnt[1] - 1]) != find(
                    A[cnt[0]][cnt[1]]):
                union(A[cnt[0]][cnt[1] - 1], A[cnt[0]][cnt[1]])
                f((cnt[0], cnt[1] - 1))

        cnt = (grid_sorted[value][0] , grid_sorted[value][1])
        f(cnt)
        value += 1
    return value - 1

grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
print(swimInWater(grid))
