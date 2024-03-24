from zad1testy import runtests
from math import inf

#max lewo biorę
def binary(Arr,s,e,x):
    last_mid = 0
    while s <= e:
        mid = (s+e)//2
        if last_mid == mid:
            break
        if Arr[mid][0] >= x:
            e = mid
        else:
            s = mid
        last_mid = mid
    if Arr[s][0] == x:
        return s
    if Arr[e][0] == x:
        return e
    return -1

def intuse( I, x, y ):
    """tu prosze wpisac wlasna implementacje"""
    n = len(I)
    dict = {}
    T = [(I[i][0],I[i][1],i) for i in range(n)]
    T = sorted(T,key = lambda x: x[0])
    parent = [[] for _ in range(n)]
    dict[y] = None
    for i in range(n):
        dict[T[i][0]] = [inf]
    for i in range(n):
        dict[T[i][1]] = []
    a = binary(T,0,n-1,x)
    if a == -1:
        return []
    for i in range(a,n):
        #sprawdzam czy dany element jest poczatkiem, lub czy już wystąpił
        if T[i][0] == x:
            dict[T[i][1]].append(T[i][2])
        else:
            if dict[T[i][0]] == [inf] or dict[T[i][0]] == []:
                continue
            else:
                dict[T[i][1]].append(T[i][2])
    result = [0 for _ in range(n)]
    if dict[y] == None:
        return []
    i = y
    stack = []
    while True:
        for el in dict[i]:
            if not result[el]:
                result[el] = 1
                stack.append(I[el][0])
        if len(stack) > 0:
            i = stack.pop()
        else:
            break
        while i is not None and i <= x:
            i = None
            if len(stack) > 0:
                i = stack.pop()
            else:
                break
        if i == None:
            break
    answear = []
    for i in range(n):
        if result[i]:
            answear.append(i)
    return answear

    
runtests( intuse )


