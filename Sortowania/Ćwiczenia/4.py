# (Pojemniki z wodą) Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami.
# Pojemniki maja kształty prostokątów, rury nie maja objetosci (powierzchni). Każdy pojemnik opisany jest
# przez współrzędne lewego górnego rogu i prawego dolnego rogu.
# Wiemy, ze do pojemników nalano A “powierzchni” wody (oczywiście woda rurami spłynęła do najniźszych
# pojemników). Proszę zaproponować algorytm Obliczający ile pojemników zostało w pełni zalanych.

#Idziemy co 1 zdarzenie (poczatek albo koniec zbiornika) najpierw je sortując (idąc w górę) i trzymamy informacje o
# aktywnych (zalewanych) zbiornikach oraz o tych juz zalanych az nasza wykorzystana na tej wysokosci objetosc nie
# osiagnie wartosci większej od nalanej wody (wtedy rozwazamy stan z poprzedniego zdarzenia) lub gdy się zrówna.
# Gdy znajdziemy poziom wody to zliczamy wszystkie w pelni zalane zbiorniki. Liniowo logarytmiczna zlozonosc
from random import randint

def MergeS(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        Left = arr[:mid]
        Right = arr[mid:]

        MergeS(Left)
        MergeS(Right)

        i, j, k = 0, 0, 0
        r, l = len(Right), len(Left)
        while r > i and l > j:
            if Right[i][0] < Left[j][0]:
                arr[k] = Right[i]
                i += 1
            else:
                arr[k] = Left[j]
                j += 1
            k += 1

        while r > i:
            arr[k] = Right[i]
            i += 1
            k += 1

        while l > j:
            arr[k] = Left[j]
            k += 1
            j += 1

def f(arr,l):
    n = len(arr)
    A = [(arr[i][1], i,True) for i in range(n)] + [(arr[i][3], i,False) for i in range(n)]
    MergeS(A)
    use = (arr[A[0][1]][2] - arr[A[0][1]][0])
    cnt = 0
    for i in range(1,2*n):
        h = A[i][0] - A[i-1][0]
        l -= (use * h)
        if l > 0:
            if A[i][2]:
               use += (arr[A[i][1]][2] - arr[A[i][1]][0])
            else:
                cnt += 1
                use -= (arr[A[i][1]][2] - arr[A[i][1]][0])

        else:
            return cnt
    return n


arr = [(randint(0,30),randint(0,30),0,0) for _ in range(10)]
for i in range(10):
    arr[i] = (arr[i][0],arr[i][1],arr[i][0]+randint(0,30),arr[i][1]+randint(0,30))
print(arr)
print(f(arr,1500))