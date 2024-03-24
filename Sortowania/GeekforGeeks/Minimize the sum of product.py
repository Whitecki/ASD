# You are given two arrays, A and B, of equal size N. The task is to find the minimum value of
# A[0] * B[0] + A[1] * B[1] + .... + A[N-1] * B[N-1], where shuffling of elements of arrays A and B is allowed

#pomysł: minimalną sumę otrzymamy wtedy kiedy jak najmniejszy wyraz z 1 tablicy przemnożymy z jak największym
# w drugiej tablicy

def minValue(self, a, b, n):
    a.sort()
    b.sort()
    suma = 0
    for i in range(n):
        suma += a[i] * b[-i - 1]
    return suma