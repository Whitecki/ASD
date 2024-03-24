'''By sprawdzić czy da się dojść z pkt a do pkt b, robie graf. Każdy koniec odcinka, o wartości x, łącze krawedzią
 skierowaną do wszystkich odcinków o wartości początkowej równej x. Następnie odpalam dfs z pkt a i sprawdzam, czy dojdzie
  do pkt b.'''

# kurcze jak zrobic w sposób sensowny, tą macierz jesli jej wartości będa np. 10**15. Normalnie oznaczało by to
# zrobienie macierzy o wymiarach k na k. Gdzie k to największa wartośc w tablicy. Normalnie dramat

def make_matrix(T):
    pass


def dfs(G):
    visited = [False for _ in range(len(G))]
    result = []
    for idx in range(len(G)):
        if not visited[idx]:
            dfsVisit(G, idx,result,visited)
    return result

def dfsVisit(G, s,result,visited):
    result.append(s)
    visited[s] = True

    for el in G[s]:
        if not visited[el]:
            dfsVisit(G, el,result,visited)

