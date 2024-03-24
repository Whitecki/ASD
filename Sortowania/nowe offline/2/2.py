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

def snow( S ):
    n  =len(S)
    Q_sort(S,0,n-1)
    i = n-1
    s = 0
    while i > -1 and S[i] - n + i + 1 > 0:
        s += (S[i] - n + i + 1)
        i -= 1

    return s

S = [1,7,3,4,1]
print(snow(S))