from zad1ktesty import runtests

"""
Algorytm:
1. iteruje przez całą tablicę, zapamiętując 3 zmienne dla każdego idx:
result[i+1] - bilans ilości jedynek minus ilość zer, dla mniejszych indeksów niż i+1
idx_min[i] - idx pod którym jest najmniejsza wartość, o mniejszym idx niż i
Time: O(n)
"""


def roznica(T):
    n = len(T)
    if T[0] == "1":
        result = -1
    else:
        result = 1
    val_min = int(T[0])
    cnt = -1
    flag = True
    for i in range(1, n):
        if T[i] == "1":
            result -= 1
        if T[i] == "0":
            result += 1
            flag = False
        val_min = min(val_min, result)
        cnt = max(result - val_min, cnt)
    if flag:
        return -1
    return max(cnt,0)


runtests(roznica)
