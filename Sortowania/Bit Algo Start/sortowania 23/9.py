
def change(a):
    boll = [0 for _ in range(10)]
    while a != 0:
        boll[a%10] += 1
        a //= 10
    jednosci = 0
    dziesietny = 0
    for el in boll:
        if el > 1:
            jednosci += 1
        if el == 1:
            dziesietny += 1
    return dziesietny*10 + jednosci

def counting_sort(T,a,n):
    A = [0 for _ in range(10)]
    result = [0 for _ in range(n)]
    for el in T:
        if a == 0:
            b = el%10
        else:
            b = el//10
        A[b] += 1
    for i in range(1,10):
        A[i] += A[i-1]
    for i in range(n):
        result[A[T[i]] - 1] = T[i]
        A[T[i]] -= 1
    T = [result[i] for i in range(n)]

def pretty_sort(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], change(T[i]))
    counting_sort(T,0,n)
    counting_sort(T,1,n)
    j,i = n-1,0
    while j > i:
        T[i],T[j] = T[j],T[i]
        j-=1
        i+=1
    return T