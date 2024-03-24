# Mamy dany nieskierowany graf G = (V, E).
# Dla każdego wierzchołka v należy wybrać liczbę naturalną f(v) (nazywaną kolorem v) tak, żeby dla każdej
# krawędzi {x, y} ∈ E zachodzilo, ze f(x) 6= f(y). Należy użyć jak najmniej kolorów (czyli zbior f(V ) powinien
# mieć minimalną liczność). Problem jest NP-zupełny więc nie istnieje optymalny algorytm wielomianowy (o
# ile P jest różne od NP). Proszę podać algorytm zachłanny, który używa najwyżej D + 1 kolorów, gdzie D to
# maksymalny stopień wierzchołka w G.

# '''
# idea:
# '''
# from queue import Queue, PriorityQueue
#
# def BFS(G,s,D):
#     Q = Queue()
#     n = len(G)
#     visited = [False for _ in range(n)]
#     visited[s] = True
#     Q.put(s)
#     q = [PriorityQueue() for _ in range(n)]
#     for el in q:
#         for i in range(D+1):
#             el.put(i)
#     while not Q.empty():
#         u = Q.get()
#         for v in G[u]:
#             q[v].get()
#             if not visited[v]:
#                 Q.put(v)
#
#     return
#
#
# '''chuj dupa nie działa'''

#2nd try
# I am going to implement Welsh Powell Algorithm

def colour_graph(G):
    #Find degree of each vertex.
    n = len(G) #O(V)
    degree = [(len(G[i]),i) for i in range(n)] #O(E)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(degree[i][0]):
            matrix[i][G[i][j]] = 1

    #List the vertices in order of descending degrees.
    degree.sort(key=lambda x:x[0], reverse=True) #O(V), bo zakres jeso od 0 do v-1

    #Colour the first vertex with color 1.
    colour = [0 for _ in range(n)]
    colour[degree[0][1]] = 1

    actclr = 1
    colour_cnt = 1
    i = 0
    while i < n:
        if not colour[i]:
            boool = [True if colour[i] else False for _ in range(n)]
            for el in degree:
                if not matrix[i][el[1]] and not boool[i]:
                    for a in G[el[1]]:
                        boool[a] = True
                    colour[el[1]] = actclr
                    colour_cnt += 1
            actclr += 1
        i += 1
        if colour_cnt == n:
            break
    return colour

G = [[1,7],
     [0,3],
     [3],
     [1,2,8,10],
     [5,10],
     [4,6],
     [5,7,10],
     [0,6,8,9,10],
     [3,7,9],
     [7,8,10],
     [3,4,6,7,9]]

a = colour_graph(G)
print(a)