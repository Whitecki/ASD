#  (uniwersalne ujście) Mówimy, że wierzchołek t w grafie skierowanym jest uniwersalnym
# ujściem, jeśli (a) z każdego innego wierzchołka v istnieje krawędź z v do t, oraz (b) nie istnieje żadna krawędź
# wychodząca z t.
# 1. Podać algorytm znajdujący uniwersalne ujście (jeśli istnieje) przy reprezentacji macierzowej (O(n))
# 2. Pokazać, że ten problem można rozwiazac w czasie O(n) w reprezentacji macierzowej.

# 1 to nudyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy, więc robię #2

def podłoga_to_jedynka(A):
    i = j = 0
    n = len(A)
    while i < n and j < n:

        if A[i][j] == 0:
            j += 1

        else:
            i += 1

    if i < j:

        for k in range(n):
            if A[i][k] != 0:
                return False
            if A[k][i] != 1 and k != i:
                return False
        return i

    elif i > j:
        for k in range(n):
            if A[i][k] != 0:
                return False
            if A[k][i] != 1 and k != i:
                return False
        return i

    else:

    while
        if A[i][k] != 0:
            return False
        if A[k][i] != 1 and k != i:
            return False
    return


nudy