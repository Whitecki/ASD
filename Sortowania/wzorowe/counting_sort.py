# T - tablica do sortowania, zakres liczb w tablicy do sortowania od 0 do k - 1
def counting_sort(T, k):
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
