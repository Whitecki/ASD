# Proszę zaproponować i zaimplementować algorytm, który mając na wejściu tablicę A zwraca
# liczbę jej inwersji (t.j., liczbę par indeksów i < j takich, że A[i] > A[j].

#liczba inwersji danego idx jest równa temu ile większych wartości stoi na lewo od niego
#Rozwiązanie: Gdy wstawiamy element z tablicy Right, podczas mergowania, zliczamy ile
# wartości z lewej tablicy zostanie postawionych po nim i dodajemy do globalnego licznika.

def MergeS(arr):
    n = len(arr)
    global cnt
    if n > 1:
        mid = n // 2
        Left = arr[:mid]
        Right = arr[mid:]

        MergeS(Left)
        MergeS(Right)

        i, j, k = 0, 0, 0
        r, l = len(Right), len(Left)
        while r > i and l > j:
            if Right[i] < Left[j]:
                arr[k] = Right[i]
                cnt += (r - i)
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



T = [5, 7, 3, 2, 1, 4]
global cnt
cnt = 0
MergeS(T)
print(cnt)
print(T)
