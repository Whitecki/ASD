#  Proszę zaproponować algorytm, który dla tablicy liczb całkowitych roz-
# strzyga czy każda liczba z tablicy jest sumą dwóch innych liczb z tablicy. Zaproponowany
# algorytm powinien być możliwie jak najszybszy. Proszę oszacować jego złożoność obliczenio-
# wą.

def binary(T,a,b,k,i):
    if r >=  l:

        q = a + (b - a)//2
        if T[a] + T[q] == T[i]:
            return q
        elif T[a] + T[q] > T[i]:
            return binary
        else:
            return q
    else:

def f(T):
    n = len(T)
    T = quicksort(T)
    for i in range(n):
        a = 0
        b = n - 1
        flag = False
        while b > a:
            if T[b] + T[a] > T[i]:
                b -= 1
            elif T[a] + T[b] < T[i]:

            else:
                flag = True
                break
        if not flag:
            return False
    return True