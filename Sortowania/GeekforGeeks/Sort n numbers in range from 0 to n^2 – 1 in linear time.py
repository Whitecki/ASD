#1 idea: every elem x in array T change in tuple. I mean for i in range(len(T)): T[i] = (T[i]//len(T),T[i]%n).
# Next we use bucket sort. we put tupples into buckets by T[i]//len(T). Then sort contents of the buckets

#2 każdy element zamieniamy na liczbe w systemie liczbowym o podstawie n. Uzyskujemy wtedy liczby naturalne dwucyfrowe.
# Radix sortem lecimy najpierw po 1, potem po 2 współrzędnej. Problem bo n > 10 to wejdą litery :(((((

# T - tablica do sortowania, zakres liczb w tablicy do sortowania od 0 do k - 1
def Counting_sort(T, k):
    n = len(T)
    # tablica wynikowa
    result = [0 for _ in range(n)]

    #C[i] - ile jest liczb równych lub mniejszych od i
    count = [0 for _ in range(k)]
    for i in range(n):
        count[T[i]] += 1
    for i in range(1, k):
        count[i] += count[i - 1]

    # element z pierwszej tablicy T wstawiam do wynikowej, pod idx wzięty z count
    for i in range(n - 1, -1, -1):
        count[T[i]] -= 1
        result[count[T[i]]] = T[i]
    # można skipnąć
    for i in range(n):
        T[i] = result[i]

def bucketSort(T,b_num):
    arr = []
    for i in range(b_num):
        arr.append([])

    # Put array elements in different buckets
    for (k,a) in T:
        indeT_b = k
        arr[indeT_b].append((k,a))

    # Sort individual buckets
    for i in range(b_num):
        arr[i] = Counting_sort(arr[i])

    # concatenate the result
    k = 0
    for i in range(b_num):
        for j in range(len(arr[i])):
            T[k] = arr[i][j]
            k += 1
    return T

def f(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i]//n,T[i]%n)
    bucketSort(T,n)


T = [1, 2, 5, 7, 5, 10, 18, 36, 18, 20, 18, 4, 21, 30, 14, 4, 37, 7, 20, 26, 39, 1, 7, 5, 12, 20, 8, 33, 28, 23, 12, 22, 14, 6, 14, 33,1,2,2,3,3]
f(T)
print(T)