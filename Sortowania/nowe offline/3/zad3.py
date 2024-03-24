from zad3testy import runtests

def radix_sort(Arr,n):
    N = len(Arr)
    for i in range(n):
        help = [[] for _ in range(26)]
        for j in range(N):
            Arr[j] = (Arr[j],ord(Arr[j][n-1-i]) - 97)
            help[Arr[j][1]].append(Arr[j])
        idx = 0
        for el in help:
            if N == idx:
                break
            for e in el:
                Arr[idx] = e[0]
                idx += 1
    idx = 0
    cnt = 1
    max_cnt = 0
    while idx < N - 1:
        if Arr[idx] == Arr[idx+1]:
            idx += 1
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            idx += 1
            cnt = 1

    return max_cnt

def strong_string(T):
    n = len(T) #O(n)
    maxi = 0
    for i in range(n): #O(N)
        T[i] = (T[i],len(T[i]),T[i][::-1])
        maxi = max(maxi,T[i][1])

    #tworze buckety #O(N)
    buckets = [[] for _ in range(maxi + 1)]

    for a,b,c in T: #O(n)
        if a > c:
            buckets[b].append(a)
        else:
            buckets[b].append(c)

    result = 0
    for i in range(maxi+1):
        if buckets[i]:
            result = max( result ,radix_sort(buckets[i],i))

    return result


# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )
