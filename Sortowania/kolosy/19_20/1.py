# Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
# jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
# że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
# cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
# liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
# 455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
# Dana jest tablica T zawierająca liczby naturalne. Proszę zaimplementować funkcję:
# pretty_sort(T)
# która sortuje elementy tablicy T od najładniejszych do najmniej ładnych. Użyty algorytm
# powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
# algorytmu oraz proszę oszacować jego złożoność czasową.


def podmianka(a):
    bol = [0 for _ in range(10)]
    while a != 0:
        bol[a%10] += 1
        a //= 10
    a,b =0,0
    for i in range(10):
        if bol[i] > 1:
            b+= 1
        elif bol[i] == 1:
            a += 1
    return (a,b)

# T - tablica do sortowania, zakres liczb w tablicy do sortowania od 0 do k - 1
def counting_sort(T,k,m):
    n = len(T)
    # tablica wynikowa
    result = [0 for _ in range(n)]

    #tablica zliczająca ile jest liczb == i, tablica pokazująca ile jest liczb równych lub mniejszych na idx i
    count = [0 for _ in range(k)]
    for i in range(n):
        count[T[i][m]] += 1
    for i in range(1,k):
        count[i] += count[i-1]
    for i in range(n-1,-1,-1):
        count[T[i][m]] -= 1
        result[count[T[i][m]]] = T[i]
    return result

def radix_sort(T):
    n = len(T)
    for i in range(n):
        T[i] = podmianka(T[i])
    T = counting_sort(T,10,1)
    T = counting_sort(T,10,0)
    return T
