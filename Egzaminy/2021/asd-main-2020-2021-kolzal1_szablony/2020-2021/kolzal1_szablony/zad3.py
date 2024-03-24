from zad3testy import runtests
from heapq import heappush
from math import inf

#pobawić się kopcami

def heapify(A,i,n):

    l,r,max_idx = 2*i + 1, 2*i + 2, i
    if l < n and A[l] > A[max_idx]:
        max_idx = l
    if r < n and A[r] > A[max_idx]:
        max_idx = r
    if max_idx != i:
        A[i], A[max_idx] = A[max_idx], A[i]
        heapify(A,max_idx,n)

def heapify_up(A,i):
    parent = (i-1)//2
    if A[parent] > A[i]:
        A[i],A[parent] = A[parent], A[i]
        return heapify_up(A,parent)
    return i


def insert(Heap,q,val,n): # wkładam, czyli daje na koniec i wykonuje heapify w górę i w dół :)
    Heap[q-1] = (val,Heap[q][1])
    heapify(Heap,heapify_up(Heap,q-1),n)

def delete(Heap,i,where_i,q):
    Heap[where_i[i]],Heap[q-1] = Heap[where_i], Heap[q-1]
    Heap[q-1] = (inf,Heap[q][1])
    where_i[i], where_i[q-1] = where_i[q-1],where_i[i]
    heapify(Heap,heapify_up(Heap,where_i[q-1]),q)


def iamlate(T, V, q, l):
    """tu prosze wpisac wlasna implementacje"""
    n = len(T)
    where_stacja = [0 for _ in range(l)]
    where_i = [-1 for _ in range(q)]
    for i in range(n):
        where_stacja[T[i]] = V[i]
    Heap = [(where_stacja[i], i) if i < min(where_stacja[0],q) else -inf for i in range(1,q+1)]
    sorted(Heap, key = lambda x: x[0], reversed = True)
    for i in range(q):
        where_i[Heap[i][1]] = i
    idx = min(where_stacja[0],q)
    # dodaje i usuwam z kopca ręcznie
    while idx < l:
        #usuwam z kopca element
        delete()
        insert()

        #dodaje nowy

        idx += 1

    return []

def iamlate(T, V, q, n):
    nwm = len(T)
    where_stacja = [0 for _ in range(n)]
    for i in range(nwm):
        where_stacja[T[i]] = V[i]
    dp = [[inf for _ in range(q)] for _ in range(n)]
    for i in range(q):
        pass
    for i in range(n):
        for last in range(i-1,max(-1,i-q),-1):
            pass




runtests( iamlate )
