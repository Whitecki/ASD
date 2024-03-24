#f(i) - najdłuższy podciąg obu zbiorów, kończący się na itym elemencie w tablicy T

def CNF(A,B):
    n = len(A)
    C = [[0 for i in range(n+1)] for i in range(n+1) ]

    for i in range(n+1):
        for j in range(n+1):

            if i == 0 or j == 0:
                continue

            else:
                if A[i - 1] == B[j - 1]:

                    C[i][j] = C[i-1][j-1] + 1

                else:

                    C[i][j] = max(C[i-1][j],C[i][j-1])

    print(C)
    return C[n][n]


A = [1,4,3,6,2,5]
B = [4,2,2,3,2,5]

c = CNF(A,B)
print(c)