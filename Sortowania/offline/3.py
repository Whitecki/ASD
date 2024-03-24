def a(T,P): #O(n) + O(k*suma)
    n = len(T) #O(n)
    Proc = [0 for _ in range(n)] #O(n)
    for i in range(len(P)): #O(k*suma długości)
        val = P[i][2] / (P[i][1] - P[i][0] + 1)
        for j in range(P[i][0],P[i][1]+1):
            Proc += val

    for i in range(n):
        if Proc[i] < int(Proc[i]) + 0.5:
            Proc[i] = int(Proc[i])
        else:
            Proc[i] = int(Proc[i]) + 1

def b(T,P):
    p = len(P)
    f_el = [P[i][0] for i in range(p)]
    f_el.sort()
    pomocnicza = []
    i = 0
    minn = P[i][1]
    while i < p:
        j = i
        while i < p-1 and f_el[i+1] == f_el[i]:
            i += 1
            minn = min(minn, P[i+1][1])

def Count(T,P,n):
    ile = [0 for _ in range(n)]
    for i in range(n):
        ile[int(T[i])] += 1
    which = ile[:]
    for i in range(1,n):
        which[i] += which[i - 1]
    return ile,which

def I_sort(A):
    pass

def B_sort(T,P):
    n = len(T)
    floor = [int(T[i]) for i in range(n)]
    ile , which = Count(T,P,n)
    arr = [[] for _ in range(which[n-1]+1)]
    for i in range(n):
        b = T[i]
        c = int(b)
        a = int((T[i] - c)*ile[c])
        arr[which[c-1]+1 + a].append(T[i])
    for i in range(n):
        arr[i].sort()
    k = 0
    for i in range(which[n-1]+1):
        for j in range(len(arr[i])):
            T[k] = arr[i][j]
            k += 1
    return T
T = [1.2, 1.5, 2.5, 3.5, 3.9, 4.5, 6.1, 7.8]
a,b = Count(T,[],8)
arr = B_sort(T,[])
print(a,b,arr)
