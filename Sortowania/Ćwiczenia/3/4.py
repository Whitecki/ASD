# k-posortowanych list scalić w jedną

class Node:
    def __init__(self):
        self.value = None
        self.next = None

def heapify(A,n,i):
    l = 2*i + 1
    r = 2*i + 2
    max_ind = i
    if l < n and A[l].val < A[max_ind].val:
        max_ind = l
    if r < n and A[r].val < A[max_ind].val:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A,n,max_ind)

def build_heap(A):
    n = len(A)
    for i in range((n-2)//2,-1,-1):
        heapify(A,n,i)

def heap_sort(A):
    n = len(A)
    build_heap(A)
    a = Node()
    start = a
    for i in range(n-1,0,-1):
        a.next = A[0]
        A[0] = A[0].next
        a = a.next
        a = a.next
        heapify(A,i,0)



