# Given an unsorted array A of size Nthat contains onlynon-negative integers, find a continuous sub-array which
# adds to a given number Sand return the left and right index(1-based indexing) of that subarray.
# In case of multiple subarrays, return the subarray indexes which comes first on moving from left to right.
# Note:- Both the indexes in the array should be according to 1-based indexing.You have to return an arraylist
# consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.

def subArraySum(arr, n, s):
    for i in range(1, n):
        arr[i] += arr[i - 1]
    T = [0 for _ in range(n)]
    T[1:n] = arr[:]

    j, i = 1, 0
    while i != n + 1 and j != n + 1 and j >= i:
        if T[j] - T[i] < s:
            j += 1
        elif T[j] - T[i] > s:
            i += 1
        else:
            if j != i:
                return (i + 1, j)
            else:
                j += 1
    return [-1]