def TS(G):
    visited = [False for _ in range(len(G))]
    result = []
    for idx in range(len(G)):
        if not visited[idx]:
            dfsVisit(G, idx,result,visited)
    result = result[::-1]
    return result
def dfsVisit(G, s,result,visited):
    visited[s] = True

    for el in G[s]:
        if not visited[el]:
            dfsVisit(G, el,result,visited)
    result.append(s)

G = [[1,2,5],
     [2,4],
     [],
     [],
     [3,6],
     [4],
     []]

def check(G,a,b):
    for el in G[a]:
        if el == b:
            return True
    return False

def Amerykanski_bohater(G):
    A = TS(G)
    i = 0
    while i < len(A) - 1:
        if not check(G,A[i],A[i+1]):
            return False
        i+=1
    return True

