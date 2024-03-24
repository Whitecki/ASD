'''
Robie MSt, a następnie zastępuje krawędzie o wadze większej niż K kasuje.
Na ich miejsce buduje lotnisko w mieście, które go nie ma,
Time: ElogV
'''
from queue import PriorityQueue

def Prima(G,startowy):
    Q = PriorityQueue()
    n = len(G)
    visited = [False for _ in range(n)]
    T = []
    visited[startowy] = True
    for v, w in G[startowy]:
        Q.put((w, startowy, v))
    while not Q.empty():
        w,v1,v2 = Q.get()
        if not visited[v2]:
            T.append([v1,v2,w])
            visited[v2] = True
            for v,w in G[v2]:
                if not visited[v]:
                    Q.put((w,v2,v))
    return T

def budowa_auuu(E:'lista krawędzi',K:'koszt lotniska',n:'ilość miast'):
    #robie liste sąsiedztwa
    G = [[] for _ in range(n)]
    for A,B,koszt in E:
        G[A].append([B,koszt])
        G[B].append([A,koszt])

    result = Prima(G,0)
    cnt = K
    for i in range(n):
        if result[i][3] > K:
            cnt += K
            result[i][3] = 0
        else:
            cnt += K
    return cnt


G = [[[1,5],[3,9],[6,3]],
     [[0,5],[2,9],[4,8],[5,6],[7,7]],
     [[1,9],[3,9],[4,4],[6,5],[7,3]],
     [[0,9],[2,9],[6,8]],
     [[1,8],[2,4],[5,2],[6,1]],
     [[1,6],[4,2],[6,6]],
     [[5,6],[3,8],[0,3],[4,1],[2,5],[7,9]],
     [[1,7],[2,3],[6,9]]]

print(Prima(G,0))