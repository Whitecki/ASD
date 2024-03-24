
def binary(Arr,x,s,e):
    if Arr[s] == x:
        return s
    if Arr[e] == x:
        return e
    while s <= e:
        mid = (s+e)//2

        if Arr[mid] == x:
                if Arr[mid-1] != x:
                    return mid
                else:
                    e = mid
        elif Arr[mid] > x:
            e = mid
        else:
            s = mid
    if Arr[e] == x:
        return e
    return False

def exer(A1, A2):
    m = len(A1)
    n = len(A2)
    A1 = A1.sort

    for i in range(n):
        a = binary(A1,A2[i],0,m-1)
        if :


