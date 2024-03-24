# You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string..
# Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.

class Node:
    def __init__(self, val):
        self.next = None
        self.val = val

    def __str__(self):
        output = ''
        output += str(self.val)
        if self.next:
            output += f' -> {self.next}'
        return output


def orderlyQueue(s, k):
    n = len(s)
    Guard = Node(None)
    End = Guard
    # jeśli wszystkie nie są wsadzone do tablicy
    for i in range(k, n):
        End.next = Node(ord(s[i]))
        End = End.next
    A = [ord(s[i]) for i in range(k)]
    min_sum = 0
    for i in range(k):
        min_sum += A[i]
    H_sort(A, Guard, End, min_sum, n, k)
    print("super",A)
    T = [_ for _ in range(n)]
    for i in range(k):
        T[i] = chr(A[i])

    for i in range(k, n):
        T[i] = chr(Guard.next.val)
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

def heapify_parent(arr, i, n):
    parent = int(((i - 1) / 2))
    if parent > 0:
        if arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            # Recursively heapify the parent node
            heapify(arr, parent, n)


def buildheap(A):
    n = len(A)
    for i in range((n - 2) // 2, -1, -1):
        heapify(A, i, n)

# wstawianie nowego elementu ogarnąć
def H_sort(A, Guard, End, min_sum, n, k):
    print(A)
    buildheap(A)
    cnt = 0
    Best = [A[i] for i in range(k)]
    while cnt < n - k + 1:
        print(cnt)
        print(Guard)
        i = k - 1
        A[0], A[i] = A[i], A[0]
        print(A)
        heapify(A, 0, i)
        print(A)
        h = A[i] + 1
        h -= 1
        End.next = Node(A[i])
        End = End.next
        A[i] = Guard.next.val
        heapify(A, 0, i)
        print(A)
        Guard.next = Guard.next.next
        cnt += 1
        if min_sum + A[i] - h < min_sum:
            min_sum = min_sum + A[i] - h
            Best = [A[j] for j in range(k)]
            cnt = 0

    A = [Best[j] for j in range(k)]


s = "baaca"
print(orderlyQueue(s, 3))
