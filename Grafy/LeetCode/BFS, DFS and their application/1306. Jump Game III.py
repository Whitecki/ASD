#Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at
# index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.
#Notice that you can not jump outside of the array at any time.
'''idea: nic wartego tłumaczenia'''
from queue import Queue

def canReach(Arr,start):
    Q = Queue()
    n = len(Arr)
    visited = [False for _ in range(n)]
    Q.put(start)
    while not Q.empty():
        u = Q.get()
        visited[u] = True
        if not Arr[u]:
            return True
        if -1 < u + Arr[u] < n and not visited[u+Arr[u]]:
            Q.put(u+Arr[u])
        if -1 < u - Arr[u] < n and not visited[u- Arr[u]]:
            Q.put(u - Arr[u])
    return False

Arr = [4,2,3,0,3,1,2]
print(canReach(Arr,5))