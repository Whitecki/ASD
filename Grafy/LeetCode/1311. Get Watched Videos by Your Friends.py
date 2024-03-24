from queue import Queue
import collections

def watchedVideosByFriends(watchedVideos, friends, id, level):
    Q = Queue()
    n = len(friends)
    visited = [False for _ in range(n)]
    visited[id] = True
    Q.put((id,0))
    result = []
    while not Q.empty():
        u,lvl = Q.get()
        if lvl == level:
            for letters in watchedVideos[u]:
                result.append(letters)
        else:
            for v in friends[u]:
                if not visited[v] and lvl <= level:
                    Q.put((v,lvl+1))
    result = set(result)
    result = sorted(result)

    return result

watchedVideos = [["A","B"],["C"],["B","C"],["D"]]
friends = [[1,2],[0,3],[0,3],[1,2]]
id = 0
level = 1
print(watchedVideosByFriends(watchedVideos,friends,id,level))
