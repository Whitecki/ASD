from bisect import bisect_left, bisect_right
def lower_bound(a, low, high, element):

    while low < high:
        mid = low + (high - low) // 2
        if element > a[mid]:
            low = mid + 1
        else:
            high = mid

    return low
def Q_sort():
    pass

def maximumIntersections(arr):
    n = len(arr)
    count = 0

    L = [arr[i][0] for i in range(n)]
    R = [arr[i][1] for i in range(n)]

    # L = Q_sort(L)
    # R = Q_sort(R)
    L.sort()
    R.sort()

    for i in range(n):
        l = arr[i][0]
        r = arr[i][1]

        cnt = lower_bound(L,0,n,l)
        cnt += (n - lower_bound(R,0,n,r+1))
        count = max(count,cnt)
    return count
# Driver Code
if __name__ == "__main__":
    L = [[1, 6],
         [5, 6],
         [2, 5],
         [8, 9],
         [1, 6]]
    a = maximumIntersections(L)
    print(a)
# This code is contributed by ukasp.