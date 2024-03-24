from queue import PriorityQueue
from math import inf


def sejf(buttons, PIN):
    time = [inf for _ in range(10000)]
    visited = [-1 for _ in range(10000)]
    Q = PriorityQueue()
    Q.put((-1, 0, -1))
    while not Q.empty():
        cnt, val, last = Q.get()
        if cnt + 1 > time[PIN]:
            break
        for el in buttons:
            a = (val + el) % 10000
            if cnt + 1 < time[a]:
                time[a] = cnt + 1
                Q.put((cnt + 1, a, val))
                visited[a] = val
    result = [PIN]
    while PIN != 0:
        result.append(PIN - visited[PIN])
        PIN = visited[PIN]
    return result[1:]
buttons = [1,2,4,8,16,32]
print(sejf(buttons,256))
