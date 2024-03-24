# dana jest posortowana rosnąco tablica A wielkości n zawierająca parami różne liczby naturalne. Podaj algorytm, który
# sprawdzi, czy jest taki indeks, że A[i]==i. Co się zmieni jeśli, liczby będą całkowite


'''
time complexity: O(logn)
idea: jeśli A[i] > i, to w posortowanej tablicy, z elementami parami różnymi, to A[i+k] > i+k
analogicznie jeśli A[i] < i, to A[i-k] < i-k
Dlatego też możemy znależć taką wartość tylko na lewo od A[i] > i oraz na prawo od A[i] < i
'''

def modified_binary_search(T):
    n = len(T)
    i,j = 0,n-1
    while j > i:
        mid = (i+j) // 2
        if T[mid] == mid:
            return mid
        elif T[mid] < mid:
            i = mid
        else:
            j = mid
    return False