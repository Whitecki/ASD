# Masz daną tablicę zawierającą n (n >= 11) liczb naturalnych w zakresie [0, k]. Zamieniono 10 liczb z tej tablicy na
#losowe liczby spoza tego zakresu (np. dużo większe lub ujemne). Napisz algorytm, który posortuje tablicę w czasie O(n).

#klasyczny counting sort, tylko sprawdzam, czy dany element pasuje do zakresu[0,k]
#Complexity = O(k+1) + O(n) + 10*log10 + 10*log10 +
from random import randint
def mod_counting_sort(A,k):
    n = len(A)
    B = [0 for _ in range(k+1)]
    less = []
    more = []
    for el in A:
        if el < 0:
            less.append(el)
        elif el > k:
            more.append(el)
        else:
            B[el] += 1
    less.sort()
    more.sort()
    m = 0
    for i in range(len(less)):
        A[i] = less[i]
        m+= 1
    p = len(more)
    for i in range(n-1,n - 1-p,-1):
        A[i] = more[p-1]
        p-=1
    for i in range(k+1):
        for j in range(B[i]):
            A[m] = i
            m+=1
    return A
#tests
for _ in range(100):
    A = [randint(0,100) for i in range(40)]
    for i in range(10):
        if i % 2 == 0:
            A.append(randint(300,500))
        else:
            A.append(randint(-23,-3))
    B = [A[i] for i in range(len(A))]
    A.sort()
    mod_counting_sort(B,100)
    if A != B:
        print(False)