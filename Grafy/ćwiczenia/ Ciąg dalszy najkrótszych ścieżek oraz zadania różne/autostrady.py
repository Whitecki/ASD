# W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć wszystkie miasta siecią autostrad, tak aby
# możliwe było dotarcie autostradą do każdego miasta. Ponieważ kontynent, na którym leży państwo jest płaski położenie
# każdego z miast opisują dwie liczby x, y, a odległość w linii prostej pomiędzy miastami liczona w kilometrach wyraża się
# wzorem len = √ (x1 − x2) 2 + (y1 − y2) 2. Z uwagi na oszczędności materiałów autostrada łączy dwa miasta w linii prostej.
# Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady zaczęto budować równocześnie i jako cel postanowiono
# zminimalizować czas pomiędzy otwarciem pierwszej i ostatniej autostrady. Czas budowy autostrady wyrażony w dniach
# wynosi ⌈len⌉ (sufit z długości autostrady wyrażonej w km). Proszę zaproponować algorytm wyznaczający minimalną liczbę
# dni dzielącą otwarcie pierwszej i ostatniej autostrady.

class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self
        self.rank = 0


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)

    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1
    return True


def kruskal(E,n,minwaga,maxwaga):
    A = [Node(i) for i in range(n)]

    count = 0
    MST = []

    for u, v, w in E:
        if union(A[u], A[v]) and minwaga <= w <= maxwaga:
            count += 1
            MST.append((u, v))
        if count == n - 1:
            break

    return MST
from math import sqrt,ceil
def f(G):
    n = len(G)
    E = []
    for i in range(n):
        for j in range(n):
            if i != j:
                E.append((i,j,ceil(sqrt((G[i][0]-G[j][0])**2 + (G[i][1]-G[j][1])**2))))
    E = sorted(E, key=lambda x: x[2])
    minimum = float("inf")
    i,j = 0,0
    while j < n:
        if kruskal(E[i:j],n,E[i][2],E[j][2]):
            print(kruskal(E[i:j],n,E[i][2],E[j][2]))
            minimum = min(j-i,minimum)
            if j == i + 1:
                j += 1
            else:
                i += 1
        else:
            j += 1
    if minimum == float("inf"):
        return False
    return minimum

P = [(5, 5), (3, -5), (0, 3), (-5, 0)]
print(f(P))