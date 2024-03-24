def Msort(T, p, k):
    if k > p:
        mid = ( p + k ) // 2

        Msort(T,p,mid)
        Msort(T,mid+1,k)
        merge(T,p,mid,k)


def merge(T, p, mid, k):

    #długości posortowanych podtablic
    l1 = mid - p + 1
    l2 = k - mid

    #tworzymy podtablice lewą i prawą
    print(l1,l2)

    Lewa = [T[p + i] for i in range(l1)]
    print(Lewa)
    Prawa = [T[mid + 1 + j] for j in range(l2)]

    i = j = 0
    n = p
    inwersje = 0
    #dopóki obie coś mają, mniejsze najpierw, z zachowaniem stabilności sortowania

    while i < l1 and j < l2:

        if Prawa[j] < Lewa[i]:
            T[n] = Prawa[j]
            inwersje += j - n
            j+=1

        else:
            T[n] = Lewa[i]
            inwersje += i - n
            i+=1

        n+=1

    while i < l1:

        T[n] = Lewa[i]
        n+=1
        i+=1

    while j < l2:
        T[n] = Prawa[j]
        n += 1
        j += 1


T = [2,3,5,8,7,1,3]

Msort(T,0,len(T))

print(T)
