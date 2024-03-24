# https://www.geeksforgeeks.org/chocolate-distribution-problem/
from math import inf


def yummy(T, m):
    T.sort()
    n = len(T)
    minimum_val = inf
    for i in range(n - m):
        minimum_val = min(minimum_val, T[i + m] - T[i])
