from queue import Queue
'''nwm kurwa czm nie działa test nr 18, to musi byc jakiś edge keys'''

def isBipartite(G):
    Q = Queue()
    n = len(G)
    colour = [-1 for _ in range(n)]
    Q.put((0,0))
    while not Q.empty():
        u, c = Q.get()
        if c:
            colour[u] = 0
        else:
            colour[u] = 1
        for v in G[u]:
            if colour[v] == colour[u]:
                return False
            if colour[v] == -1:
                Q.put((v,colour[u]))
    return True

G = [[2,3],
     [3],
     [0,3],
     [0,1,2]]
a = isBipartite(G)
print(a)