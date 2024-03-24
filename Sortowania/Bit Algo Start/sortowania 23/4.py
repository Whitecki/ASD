# Dana jest nieskończona tablica A, gdzie pierwsze n pozycji zawiera posortowane liczby naturalne, a reszta tablicy ma
# wartości None. Nie jest dana wartość n. Przerdstaw algorytm, który dla danej liczby naturalnej x znajdzie indeks w tablicy,
# pod którym znajduje się wartość x. Jeżeli nie ma jej w tablicy, to należy zwrócić None.

# zadanie tak proste, że aż szkoda czasu na klepanie
#iteruje, aż dotre do wartości None, wtedy wiem jaka jest długość podtablicy z samymi wartościami liczbowymi.
# następnie puszczam binary searcha i mam.

# mozna by też znależć tą liczbę szybciej, np.logn
from math import inf

def binary(Arr,x,s,e):
    while s <= e:
        mid = (s+e)//2

        if Arr[mid] == x:
            return mid
        elif Arr[mid] > x:
            e = mid
        else:
            s = mid
    return False

def f(A,x):
    if A[0] == x:
        return 0
    if A[1] ==x:
        return 1

    i = 0
    flag = True
    start = 0
    finish = inf
    while flag and finish > start:
        if A[start + 2**i] is not None:
            if A[start + A ** i] < x:
                i += 1
            else:
                finish = min(finish,start + 2**i)
                flag = False

        else:
            start += 2 ** (i-1)
            finish = min(finish,2**i)
            i = 1


    result = binary(A,x,start,finish)

    if result:
        return result
    return None