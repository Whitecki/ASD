from math import inf
from heapq import heappush, heappop


def heapify(Heap, Gdzie_w_kopcu, i, n):
    l, r, max_idx = 2 * i + 1, 2 * i + 2, i

    if l < n and Heap[l][0] < Heap[max_idx][0]:
        max_idx = l
    if r < n and Heap[r][0] < Heap[max_idx][0]:
        max_idx = r

    if max_idx != i:
        Heap[i], Heap[max_idx] = Heap[max_idx], Heap[i]
        Gdzie_w_kopcu[Heap[i][1]], Gdzie_w_kopcu[Heap[max_idx][1]] = Gdzie_w_kopcu[Heap[max_idx][1]], Gdzie_w_kopcu[Heap[i][1]]
        heapify(Heap, Gdzie_w_kopcu, max_idx, n)


def heapify_up( Heap, Gdzie_w_kopcu, i):
    max_idx = (i - 1) // 2
    if max_idx > -1 and Heap[i][0] < Heap[max_idx][0]:
        Heap[i], Heap[max_idx] = Heap[max_idx], Heap[i]
        Gdzie_w_kopcu[Heap[i][1]], Gdzie_w_kopcu[Heap[max_idx][1]] = Gdzie_w_kopcu[Heap[max_idx][1]], Gdzie_w_kopcu[Heap[i][1]]
        return heapify_up(Heap,Gdzie_w_kopcu, max_idx)
    return i


def delete(Heap, Gdzie_w_kopcu, L, d):  # usuwam i-ty element
    Heap[d], Heap[L - 1] = Heap[L - 1], Heap[d]
    Heap[L-1] = (inf, Heap[L-1][1])
    Gdzie_w_kopcu[Heap[d][1]], Gdzie_w_kopcu[Heap[L - 1][1]] = Gdzie_w_kopcu[Heap[L - 1][1]], Gdzie_w_kopcu[Heap[d][1]]
    heapify(Heap, Gdzie_w_kopcu, heapify_up(Heap, Gdzie_w_kopcu, d), L)


def insert(T, Heap, Gdzie_w_kopcu, L, i):
    Heap[L - 1] = (T[i], Heap[L-1][1])
    heapify(Heap, Gdzie_w_kopcu, heapify_up(Heap, Gdzie_w_kopcu,L - 1), L)


def stacja(T, L):
    n = len(T)
    Gdzie_w_kopcu = [-1 for i in range(L)]
    Heap = []
    idx, koszt = L, 0
    for i in range(L):
        heappush(Heap, (T[i], i))
        a, b = heappop(Heap)
        koszt += a
        heappush(Heap, (a, b))
    for i in range(L):
        Gdzie_w_kopcu[Heap[i][1]] = i
    while idx + 1 < n:
        delete(Heap, Gdzie_w_kopcu, L, Gdzie_w_kopcu[idx % L])
        insert(T, Heap, Gdzie_w_kopcu, L, idx)
        koszt += Heap[0][0]
        idx += 1
    return koszt


T = [7, inf, 4, 8, inf, 6, 1, inf, inf]
L = 5

print(stacja(T, L))
