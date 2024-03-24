def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def Q_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        Q_sort(A, p, q - 1)
        Q_sort(A, q + 1, r)


