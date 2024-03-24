
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