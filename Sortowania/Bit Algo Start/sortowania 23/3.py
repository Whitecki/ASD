# Dana jest tablica liczb rzeczywistych wielkości n reprezentująca kopiec minimum (array-based-heap). Mając daną liczbę
# rzeczywistą x sprawdź, czy k-ty najmniejszy element jest wiekszy lub równy x

"idea1: wyciągamy z kopca najmniejszy element, naprawiamy go, aż usyzkamy k najmniejszy element wtedy wystarczy porównac z x"
"time complexity: klogn"

def heapify(A,i,n):
    l = 2*i+1
    r = 2*i+2
    max_idx = i
    if l < n and A[l] > A[max_idx]:
        max_idx = l
    if r < n and A[r] > A[max_idx]:
        max_idx = r
    if max_idx != i:
        A[i], A[max_idx] = A[max_idx], A[i]
        heapify(A,max_idx,n)

def heap_sort(T,k):
    n = len(T)
    if k == 1:
        return min(T)
    for i in range(n-1,n-k,-1):
        T[0], T[i] = T[i], T[0]
        heapify(T,0,i)