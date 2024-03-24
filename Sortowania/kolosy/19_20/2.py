# Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
# podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
# wzrostu. Proszę zaimplementować funkcję:
# section(T,p,q)
# która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.

def partition(T, p, r):
    x = T[r]
    i = p - 1
    for j in range(p, r):
        if T[j] <= x:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i + 1], T[r] = T[r], T[i + 1]
    return i + 1

def select(T, p, r, k):
    if p == r:
        return T[p]
    q = partition(T, p, r)
    if q == k:
        return T[q]
    elif k < q:
        return select(T, p, q - 1, k)
    else:
        return select(T, q + 1, r, k)

def f(T,p,q):
    if p > q:
        p,q = q,p
    n = len(T)
    a = select(T,0,n,p)
    b = select(T,0,n,q)
    result = [0 for _ in range(b- a)]
    j = 0
    for i in range(n):
       if T[b] >= T[i] >= T [a]:
           result[j] = T[i]
           j += 1
    return result