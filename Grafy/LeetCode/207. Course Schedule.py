# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
# prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

# Return true if you can finish all courses. Otherwise, return false.

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

def f(numCourses, prerequisites):

    #transform prerequisites to graph
    G = [[] for _ in range(numCourses)]
    input = [0 for _ in range(numCourses)]
    for v,u in prerequisites:
        G[u].append(v)
        input[v] += 1

    #sortuje topologicznie graf, warunki spełnia tylko DAG, więc essa
    result = TS(G)

    #tablica mówiąca nam gdzie jest wierzchołek po sortowaniu topologicznym
    where = [-1 for _ in range(numCourses)]
    for i in range(numCourses):
        where[result[i]] = i

    #muszą wszystkie krawędzie być "skierowane w prawo"
    #dodatkowo mogę wejść tylko wtedy do wierzchołka gdy nie wchodzi nic do niego, lub wchodzące już odwiedziłem
    #wchodząc do danego wierzchołka mogę wejśc do następnych XD
    for vertex in result:
        if input[vertex] > 0:
            return False
        for edge in G[vertex]:
            input[edge] -= 1

    return True



numCourses = 2
prerequisites = [[1,0],[0,1]]
print(f(numCourses,prerequisites))


