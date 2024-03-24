# Dana jest tablica z n liczbami całkowitymi. Zawiera ona bardzo dużo powtórzeń - co więcej, zaledwie O(log(n)) liczb
# jest unikatowe (reszta to powtórzenia). Napisz algorytm, który w czasie O(n*log(log(n))) posortuje taką tablicę.

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

def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def Q_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        Q_sort(A, p, q - 1)
        Q_sort(A, q + 1, r)




# robimy tablice z samymi unikalnymi liczbami. Iterując po całej tablicy sprawdzamy binnary searchem czy dany element już się
#pojawił, jeśli tak to sortujemy elementy w tablicy
def unique(A):
    n = len(A)
    uniq = []
    m = 0
    for i in range(n):
        if binary(uniq,A[i],0,m):
            uniq.append(A[i])
            m += 1
            Q_sort(uniq,0,m-1)
    return uniq

# dalej robimy coś ala counting sort