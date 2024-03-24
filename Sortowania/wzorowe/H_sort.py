def heapify(A,i,n):
    l = 2*i+1
    r = 2*i + 2
    max_idx = i
    if l < n and A[l] > A[max_idx]:
        max_idx = l
    if r < n and A[r] > A[max_idx]:
        max_idx = r
    if max_idx != i:
        A[i],A[max_idx] = A[max_idx],A[i]
        heapify(A,max_idx,n)

def buildheap(A):
    n = len(A)
    for i in range((n-2)//2,-1,-1):
        heapify(A,i,n)

def H_sort(A):
    n = len(A)
    buildheap(A)
    for i in range(n-1,0,-1):
        A[0],A[i] = A[i], A[0]
        heapify(A,0,i)
        print(A[i])

T = [8,7,10,5,2,3,0,1]
H_sort(T)
print(T)