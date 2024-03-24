# Mamy daną tablicę stringów, gdzie suma długości wszystkich stringów daje n. Napisz algorytm, który posortuje tę tablicę
# w czasie O(n). Można założyć, że stringi składają się wyłącznie z małych liter alfabetu łacińskiego.

def bucket_sort(A):
    m = len(A)
    T = [[] for _ in range(m)]
    for el in A:
        n = len(el)
        T[n].append(el)
    