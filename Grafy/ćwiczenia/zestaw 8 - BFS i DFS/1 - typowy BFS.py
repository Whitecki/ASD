from queue import Queue

def delete_vertices(graph, source):
    queue = Queue()
    visited = [False] * len(graph)
    visited[source] = True
    result = [source]
    queue.put(source)
    while not queue.empty():
        u = queue.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                queue.put(v)
                result.append(v)
    result.reverse()

    return result

graph = [[1, 2], [0, 3, 4], [0, 6, 7, 8], [1, 5], [1], [3], [2], [2], [9, 10], [8], [8]]
print(delete_vertices(graph, 0))
