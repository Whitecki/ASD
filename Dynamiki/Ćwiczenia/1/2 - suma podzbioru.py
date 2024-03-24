# Zadanie 2. (problem sumy podzbioru) Dana jest tablica n liczb naturalnych A. Proszę podać
# i zaimplementować algorytm, który sprawdza, czy da się wybrać podciąg liczb z A, które sumują się do zadanej
# wartości T.

# czy da się zbudować liczbę x z przedziału (0, ...., suma) z kolejnych liczb

def hindus_wytłumaczył(A, suma,wyniki):
    n = len(A)
    DP = [[False for _ in range(suma + 1)] for i in range(n)]

    for i in range(n):
        DP[i][0] = True

    DP[0][A[0] + 1] = True
    flag = False
    for i in range(n):
        for j in range(suma + 1):

            if A[i] > j:
                DP[i][j] = DP[i - 1][j]

            else:

                DP[i][j] = (DP[i - 1][j] or DP[i - 1][j - A[i]])

        if DP[i][suma] == True:
            return True
    #
    # # zwrócimy sb jakie liczby były użyte
    #
    # i = n - 1
    # j = suma
    # while i > 0 and j > 0:
    #
    #     if DP[i - 1][j] == True:
    #         i -= 1
    #
    #     else:
    #         wyniki.append((i,j))
    #         i -= 1
    #         j -= A[i]
    #         wyniki.append((i, j))
    # print(i)

    return False


T = [14, 5, 19, 3, 20, 14, 8, 7, 2]
s = 34
# :3
wyniki = []
fajny = hindus_wytłumaczył(T, s,wyniki)
print(fajny)
print(wyniki)