from math import inf
# tablica n elementowa, szukamy maximum i minimum w 1,5n porównań.
#idea: dziel i zwyciężaj(robimy podproblemy!): mamy średnio półtora porównania na jeden idx, czyli 3 porównania na 2 idx.
# jak znależć maksymalny i minimalny element 4 elementów ? Porównujemy dwa elementy w tablicy ze sobą, mniejszy
# porównujemy z mniejszym, większy z większym. ale słaby oopis ^^
def f(T):
    n = len(T)
    gus = T[-1]
    zus = T[-1]
    for i in range(1,n,2):
        if T[i] > T[i-1]:
            mi,ma = T[i-1],T[i]
        else:
            mi,ma = T[i],T[i-1]

        gus = min(mi,gus)
        zus = max(ma,zus)
    return gus, zus


T=[1,2,3]
print(T[-1])