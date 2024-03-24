def f(A, B, C):
    a, b, c = len(A), len(B), len(C)
    d = max(a, b, c)
    if a == d:
        B.sort()
        C.sort()
    elif b == d:
        A.sort()
        C.sort()
        A, B = B, A
        a, b = b, a
    else:
        B.sort()
        A.sort()
        A, C = C, A
        a, c = c, a
        # a jest najdłuższym teraz

    for el in A:
        i,j = 0,c-1
        while i < b and j > -1:
            if B[i] + C[j] > el:
                j -= 1
            elif B[i] + C[j] < el:
                i += 1
            else:
                return True
    return False
