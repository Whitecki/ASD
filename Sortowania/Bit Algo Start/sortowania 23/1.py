# Dane są dwa zbiory liczb, reprezentowane jako tablice rozmiarów m i n, gdzie m jest znacznie mniejsze od n. Zaproponuj
# algorytm, który sprawdzi, czy zbiory są rozłączne.

#sortuje mniejszą tablice, następnie iteruje po większej tablicy i sprawdzam czy dany element również znajduje się w
#mniejszej tablicy za pomocą binarry_search
#Time complexity: O(n+m)logm ~ n, bo m <<< n

def binary(Arr,x,s,e):
    while s <= e:
        mid = (s+e)//2

        if Arr[mid] == x:
            return mid
        elif Arr[mid] > x:
            e = mid
        else:
            s = mid
    return False

def f(M,N):
    m,n = len(M), len(N)
    M.sort()

    for i in range(n):
        if not binary(M,N[i],0,m-1):
            return False

    return True

