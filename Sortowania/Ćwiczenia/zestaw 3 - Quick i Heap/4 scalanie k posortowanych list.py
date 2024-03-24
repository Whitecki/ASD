#naprawmy pociągnijmy w dół i-ty element

def napraw(A,n,i):

    l = 2*i + 1
    p = 2*i + 2
    min_ind = i

    if l < n and A[l] < A[min_ind]:
        min_ind = l

    if p < n and A[p] < A[min_ind]:
        min_ind = p

    if min_ind != i:
        A[i], A[min_ind] = A[min_ind], A[i]

        napraw(A,n,min_ind)

# budujemy kopiec, czyli naprawiamy wszystkie elementy od połowy

def buduj(A):

    n = len(A)

    for i in range(((n-2)//2),-1,-1):
        napraw(A,n,i)


def zad4(T):
    n = len(T)

    # tworzę tablicę z pierwszymi elementami danej tablicy
    pierwsi = [(T[i][0],i) for i in range(n)]
    print(pierwsi)

    # buduje kopiec
    buduj(pierwsi)

    #tworzymy listę z posortowanymi liczbami
    fajrant = []

    #dopóki nie skończy się lista
    while len(pierwsi) != 0:
        print(pierwsi.pop(0))
        #wyciągamy najmniejszy element z góry kopca i jego index
        najmniejszy, index = pierwsi.pop(0)

        # wyjęty element z kopca(pierwsi) usuwamy z pierwotnej listy(T)
        T[index].pop(0)

        # znowu robimy by najmniejszy element był na górze
        napraw(pierwsi,len(pierwsi) - 1, 0)

        # wstawiamy najmniejszy element do listy wynikowej
        fajrant.append(najmniejszy)

        # trzeba jakoś wstawiać nowe elementy
        if len(T[index]) != 0:
            pierwsi.append(T[index][0])

    return fajrant

T = [[3, 17, 24, 49], [2, 5], [31, 52], [8, 8, 27]]
print(zad4(T))





