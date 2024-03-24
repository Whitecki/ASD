def MergeS(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        Left = arr[:mid]
        Right = arr[mid:]

        MergeS(Left)
        MergeS(Right)

        i, j, k = 0, 0, 0
        r, l = len(Right), len(Left)
        while r > i and l > j:
            if Right[i] < Left[j]:
                arr[k] = Right[i]
                i += 1
            else:
                arr[k] = Left[j]
                j += 1
            k += 1

        while r > i:
            arr[k] = Right[i]
            i += 1
            k += 1


        while l > j:
            arr[k] = Left[j]
            k += 1
            j += 1