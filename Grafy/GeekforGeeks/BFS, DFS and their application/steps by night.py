from queue import PriorityQueue
from math import inf
def minStepToReachTarget(KnightPos, TargetPos, n):
    Q = PriorityQueue()
    i,j = KnightPos
    Q.put((0,i,j))
    visited = [[inf for _ in range(n)] for _ in range(n)]
    while not Q.empty():
        cnt,i,j = Q.get()
        visited[i][j] = cnt
        for moves in [(1,2),(2,1),(-1,2),(1,-2),(-2,-1),(-2,1),(-1,-2),(2,-1)]:
            if n > i + moves[0] > -1 and n > j + moves[1] > -1 and visited[i+moves[0]][j+moves[1]] > cnt + 1:
                Q.put((cnt+1,i+moves[0],j+moves[1]))
    if visited[TargetPos[0]][TargetPos[1]] == inf:
        return -1
    return visited[TargetPos[0]][TargetPos[1]]

print(minStepToReachTarget((0,2),(1,1),3))

