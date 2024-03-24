#w chuj (bardzo) trudne

#dostaje ciąg złożony z liczb całkowitych, pomiędzy którymi znajdują się operatory dodawania i mnożenia, mamy powstaiwać
#tak nawiasy by zmaksymalizować wynik

from math import inf

def nawiasy(T:"ciag: 'a $ b $ c $ d $ .... $ z', gdzie $ to operator, litera to liczba całkowita "):
    n = len(T)
    operator = ["+" if T[i] == "+" else "*" for i in range(1, n, 2)]
    liczba = [int(T[i]) for i in range(0, n, 2)]
    dp = [[inf if j!=i else liczba[i] for j in range(n // 2 + 1)] for i in range(n // 2 + 1)] #minimal value
    DP = [[-inf if j!=i else liczba[i] for j in range(n // 2 + 1)] for i in range(n // 2 + 1)] #maximal value

    #topological order, czyli musze iść od jak najmniejszych podprzedziałów, by robić to iteracyjne :))))
    for dlugosc in range(1,n//2 + 1): #długość podprzedziału, zaczynamy od 1, i idziemy do n
        for start in range(0,n//2-dlugosc+1): # podprzedział zaczynający się na j i kończący na j+i
            i = start
            j = start + dlugosc
            for root in range(i,j): #O(n) bo przelatuje przez potencjalnie wszystkie możliwe root-y

                if operator[root] == "+":
                    dp[i][j] = min(dp[i][root] + dp[root+1][j],dp[i][j])
                    DP[i][j] = max(dp[i][root] + dp[root+1][j],DP[i][j])
                else:
                    dp[i][j] = min(DP[i][root] * DP[root + 1][j],dp[i][j])
                    DP[i][j] = max(DP[i][root] * DP[root + 1][j],DP[i][j])

    return DP[0][n//2], dp[0][n//2]


expression = "7+4*3+5"
print(nawiasy(expression))