def depth(T):
    def partition(T, p, r, index):
        pivot = T[r][index]
        i = p - 1
        for j in range(p, r):
            if T[j][index] <= pivot:
                i += 1
                T[i], T[j] = T[j], T[i]
        T[i + 1], T[r] = T[r], T[i + 1]
        return i + 1

    def quicksort(T, p, r, index):
        while p < r:
            q = partition(T, p, r, index)
            if q - p <= r - q:
                quicksort(T, p, q - 1, index)
                p = q + 1
            else:
                quicksort(T, q, r, index)
                r = q - 1

    def the_most_intervals(T):
        n = len(T)
        quicksort(T, 0, n - 1, 0)
        for i in range(n):
            T[i] = (T[i][0], T[i][1], i)
        quicksort(T, 0, n - 1, 1)
        for i in range(n):
            T[i] = (T[i][0], T[i][1], T[i][2], i)
        max_interval = 0
        for i in range(n):
            if T[i][3] - T[i][2] > max_interval:
                max_interval = T[i][3] - T[i][2]
        return max_interval

    return the_most_intervals(T)
arr = [[1, 6], [5, 6], [2, 5], [8, 9], [1, 6]]
n = len(arr)
print(depth(arr))