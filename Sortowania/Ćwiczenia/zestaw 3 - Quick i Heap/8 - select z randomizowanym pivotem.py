from random import randint

def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    x = randint(low, high)
    T[high], T[x] = T[x], T[high]
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller
        # than or equal to pivot
        if arr[j] <= pivot:
            # increment index of
            # smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


def select(A,p,k,r):

    if p == r:

        return A[p]

    if p < r:

        q = partition(A,p,k)

        if q == k:
            return A[q]

        elif q < k:
            return select(A,q+1,k,r)

        else:
            return select(A,p,k,q-1)

T = [0,1,2,3,4,5,6,7,8,9,10,11,12]
a = select(T,0,8,len(T)-1)
print(a)