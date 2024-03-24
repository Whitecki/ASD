def f(boombs):

    #robię graf
    n = len(boombs) #O(V^2)
    G = [[] for _ in range(n)]
    for i in range(n):
        X,Y,R = boombs[i]
        j = 0
        for (x,y,r) in boombs:
            a,b = (X-x)**2,(Y-y)**2
            if a + b < R:
                G[i].append(j)
            j+=1

    #zliczam te wierzchołki do których nic nie wchodzi #O(E)
    start = [True for _ in range(n)]
    for edges in G:
        for edge in edges:
            start[edge] = False



    #DFS odpalam, który zlicza ile bomb zostanie zdetonowanej, po detonacji i-tej. Początkowe wierzchołki to takie które mają
    def dfsVisit(G, s, result, visited):
        visited[s] = True

        if result[s] != -1:
            return result[s]

        suma = 0
        for el in G[s]:
            a = dfsVisit(G, el, result, visited)
            result[s] += a
            if not visited[el]:
                suma += a

        return max(suma,1)
    # w visited pisze z którego dfs udało mi się tu dojść
    visited = [False for _ in range(len(G))]
    result = [-1 for i in range(n)]
    for idx in range(len(G)):
        if not visited[idx] and start[idx]:
            dfsVisit(G, idx, result, visited)
## nieskończone





