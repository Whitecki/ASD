# Dany jest ciąg przedziałów domkniętych [a1, b1], . . . ,[an, bn]. Proszę
# zapropnować algorytm, który znajduje taki przedział [at, bt], w którym w całości zawiera się jak najwięcej
# innych przedziałów.

# Rozwiązanie: odcinek x(b,e),o początku w pkt. b i końcu w pkt. e, zawiera się w odcinku X(B,E),  <=> b>=B i e<=E
# z zasady kontrapozycji wynika: że gdy b < B lub e > E, to odcinek x nie zawiera się w X
#
from random import randint


def MergeS(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        Left = arr[:mid]
        Right = arr[mid:]

        MergeS(Left)
        MergeS(Right)

        i, j, k = 0, 0, 0
        r, l = len(Right), len(Left)
        while r > i and l > j:
            if Right[i][0] < Left[j][0]:
                arr[k] = Right[i]
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


def it_does_not_works(arr):
    n = len(arr)
    A = [(arr[i][0],i) for i in range(n)] + [(arr[i][1],i) for i in range(n)]
    MergeS(A)
    T = [False for _ in range(n)]
    cnt = 0
    m_cnt = 0
    for i in range(2*n):
        if not T[A[i][1]]:
            T[A[i][1]] = True
            cnt += 1
        else:
            T[A[i][1]] = False
            cnt -= 1
        m_cnt = max(m_cnt,cnt)
    return m_cnt

arr = [(randint(0,25),0) for i in range(10)]
for i in range(10):
    arr[i] = (arr[i][0],arr[i][0] + randint(0,25))

def binary(Arr,x,s,e):
    while s <= e:
        mid = (s+e)//2

        if Arr[mid] == x:
            return mid
        elif Arr[mid] > x:
            e = mid
        else:
            s = mid
    return mid
def between(A,idx):
    pass

def f(arr):
    n = len(arr)
    L = [(arr[i][0], i) for i in range(n)]
    R = [(arr[i][1], i) for i in range(n)]
    MergeS(L)
    MergeS(R)
    T = [(0,0) for _ in range(n)]

    val = [0 for _ in range(n)]
    i = n - 1
    while i > -1:
        val[R[i][1]] += (n - i - 1)
        j = 1
        while i - j > -1 and R[i][0] == R[i - j][0]:
            val[R[i - j][1]] += (n - i - 1)
            j += 1

        i -= max(1,j)
    i = 0
    while i < n:
        val[L[i][1]] += i
        j = 1
        while i + j < n and L[i][0] == L[i + j][0]:
            val[L[i + j][1]] += i
            j += 1
        i += max(1,j)
    A = [(arr[i][0], i,True) for i in range(n)] + [(arr[i][1], i,False) for i in range(n)]
    MergeS(A)
    for i in range():
        pass



    return max(val)


f(arr)