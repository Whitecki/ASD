from math import inf
#ej bo to na listach jest zrobione
def kocham_kube(T, k):
    n = len(T)
    he_lp_ap = [T[i] for i in range(k)]
    buildheap(he_lp_ap)
    m = 0
    # póki da się dokładać do kopca
    for i in range(n - (k + 1)):
        heapify(he_lp_ap, k + 1, 0)
        T[m] = he_lp_ap[0]
        m += 1
        he_lp_ap[0] = T[k + 1 + m]

    for i in range(k + 1):
        heapify(he_lp_ap, k + 1 - i, 0)
        T[m] = he_lp_ap[0]
        m += 1
        he_lp_ap[0], he_lp_ap[k - i] = he_lp_ap[k - 1], -inf


def heapify(A, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    m = i
    if l < n and A[l] < A[m]:
        m = l
    if r < n and A[r] < A[m]:
        m = r
    if m != i:
        A[i], A[m] = A[m], A[i]
        heapify(A, n, m)


# budujemy kopiec binarny
def buildheap(A):
    n = len(A)
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)
