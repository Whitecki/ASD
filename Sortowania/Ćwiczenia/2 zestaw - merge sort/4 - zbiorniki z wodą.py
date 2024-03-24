#Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami.
#Pojemniki maja kształty prostokątów, rury nie maja objetosci (powierzchni). Każdy pojemnik opisany jest
#przez współrzędne lewego górnego rogu i prawego dolnego rogu.
#Wiemy, ze do pojemników nalano A “powierzchni” wody (oczywiście woda rurami spłynęła do najniźszych
#pojemników). Proszę zaproponować algorytm Obliczający ile pojemników zostało w pełni zalanych.

def woda(T, A):
    j = 0
    licznik = 0
    aktualna_ilość_wody = A
    koszt_teraz = 0
    dolna = 0
    górna = 0
    n = len(T)
    for i in range(n):
        górna = T[j][0]
        koszt_teraz = 0
        if j >= 1:
            dolna = T[j-1]

        if górna > T[i][1][0] and dolna < T[i][0][0]:

            koszt_teraz += (górna - dolna) * (T[i][1][1] - T[i][0][1])


