# Dana jest tablica zawierająca n liczb z zakresu [0...n^2-1]. Napisz algorytm, który posortuje taką tablicę w czasie O(n).

''''idea: zamieniam liczby w reszte z dzielenia przez n(A[i]= A[i]%n) i sortuje kubełkowo. Następnie sortuje po wartościach
 dzielenia całkowitoliczbowego. Radix sort najpier po wartościach modulo, nastepnie po liczbach podzielonych całkowitoliczbowo
 Time complexiti: O(n)'''

from random import randint

def sort_numb_to_n_square(T):
    n = len(T)
    rest = [[] for _ in range(n)]
    base_of_power = [[] for _ in range(n)]
    for el in T:
        rest[el%n].append(el)
    idx = 0
    for elements in rest:
        for el in elements:
           T[idx] = el
           idx += 1

    for el in T:
        base_of_power[el//n].append(el)
    idx = 0
    for elements in base_of_power:
        for el in elements:
           T[idx] = el
           idx += 1

    return T

n = 20
T = [randint(0,n**2) for _ in range(n)]
sort_numb_to_n_square(T)
print(T)