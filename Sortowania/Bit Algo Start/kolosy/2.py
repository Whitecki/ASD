# You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string..
# Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


def orderlyQueue(s, k):
    n = len(s)
    Guard = Node(None)
    End = Guard
    # jeśli wszystkie nie są wsadzone do tablicy
    for i in range(k, n):
        End.next = Node(ord(s[k]))
        End = End.next
    A = [ord(s[i]) for i in range(k)]
    min_sum = 0
    for i in range(k):
        min_sum += A[i]
    H_sort(A, Guard, End, min_sum, n, k)
    print(A)
    for i in range(k):
        s[i] = chr(A[i])

    for i in range(k, n):
        s[i] = chr(Guard.next.val)
        Guard = Guard.next


def heapify(A, i, n):
    l = 2 * i + 1
    r = 2 * i + 2
    max_idx = i
    if l < n and A[l] > A[max_idx]:
        max_idx = l
    if r < n and A[r] > A[max_idx]:
        max_idx = r
    if max_idx != i:
        A[i], A[max_idx] = A[max_idx], A[i]
        heapify(A, max_idx, n)


def buildheap(A):
    n = len(A)
    for i in range((n - 2) // 2, -1, -1):
        heapify(A, i, n)


def H_sort(A, Guard, End, min_sum, n, k):
    buildheap(A)
    cnt = 0
    print(A)
    B = [A[i] for i in range(k)]
    while cnt < n - k +1:
        i = k - 1
        if min_sum + Guard.next.val - A[0] < min_sum:
            min_sum = min_sum + Guard.next.val - A[0]
            B = [A[i] for i in range(k)]
            cnt = 0
        End.next = Node(A[0])
        End = End.next
        print(Guard.next.val, cnt)
        A[0] = Guard.next.val
        Guard.next = Guard.next.next
        A[0],A[i] = A[i],A[0]
        print(A)
        heapify(A, 0, i)
        cnt += 1
        print(A)
    A = [B[i] for i in range(k)]


print(int(((0 - 1) / 2)))
