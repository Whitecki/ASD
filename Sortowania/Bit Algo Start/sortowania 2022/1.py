# Mamy dane n punktów (x, y) w okręgu o promieniu k (liczba naturalna), tzn. 0 <= x2 + y2 <= k, które są w nim
# równomiernie rozłożone, tzn. prawdopodobieństwo znalezienia punktu na danym obszarze jest proporcjonalne do pola tego obszaru.
# Napisz algorytm, który w czasie Θ(n) posortuje punkty po ich odległości do punktu (0, 0), tzn. d = sqrt(x2 + y2).
from math import sqrt
def normalisation(n,k,val):
    pass

def Fast_sort(A):
    pass

def Insertion_sort(A):
    pass

def circle_sort(T,k):
    n = len(T)
    A = [[] for _ in range(n)]
    for el in T:
        val = sqrt((el[0])**2+(el[1])**2)
        which_cub = int(normalisation(n,k,val))
        A[which_cub].append(el)

    for el in A:
        if len(el) < 10:
            Insertion_sort(el)
        else:
            Fast_sort(el)

    i = 0
    for el in A:
        for j in range(len(el)):
            T[i] = el[j]
            i += 1

    return T


