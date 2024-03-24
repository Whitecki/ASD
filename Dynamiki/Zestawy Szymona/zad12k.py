from zad12ktesty import runtests 
from math import inf
#minmax
def autostrada( T, k ):
    #Tutaj proszę wpisać własną implementację
    n = len(T)
    A = [0 for _ in range(n)]
    A[n-1] = 1
    sum = [T[i] for i in range(n)]
    for i in range(1,n):
        sum[i] = sum[i] + sum[i-1]
    for K in range(k):
        s,e = 0,0
        max_sum = 0
        max_s, max_e = 0,0
        # znajduje największy obszar, do podzielenia
        while e < n-1:
            s = e
            while not A[e]:
                e += 1
            if max_sum < sum[e] - sum[s] - T[s] and s != e:
                max_sum = sum[e] - sum[s] - T[s]
                max_s = s
                max_e = e
                s,e = e+1,e+1
        if K + 1 == k:
            return sum[max_e] - sum[max_s] - T[max_s]
        max_podzial, kk = inf, s
        for i in range(max_s,max_e):
            if max_podzial > max(sum[i]-sum[max_s]+T[max_s], sum[max_e] - sum[i]):
                max_podzial = max(sum[i]-sum[max_s]+T[max_s], sum[max_e] - sum[i])
                kk = i

        A[kk] = 1

    return sum()

runtests ( autostrada,all_tests=False )