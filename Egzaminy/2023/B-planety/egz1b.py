from egz1btesty import runtests
from math import inf

"""
Opis:
definiuje funkcję dp(i,b) - minimalny koszt dolecenia do i-tej planety, mając dokładnie b paliwa

Jeśli w baku mam 0 paliwa to sprawdzam, co opłaca się bardziej. Przylecieć z poprzedniej planety, oddalonej o x
odległości, gdzie miałem x paliwa, czy bardziej opłaca się przeteleportować (o ile się da).

Jeśli w baku mam więcej niż 0 paliwa, to sprawdzam czy bardziej opłaca się dotankować 1 jednostkę paliwa i zapłącić za nie
na i-tej planecie, czy przylecieć z poprzedniej, gdzie miałem paliwa więcej o tyle, ile wynosi różnica pomiędzy tymi planetami

Jeśli jestem na pierwszej planecie, dp(i,b) = b*C[0]

Rozwiązaniem problemu jest min(dp(n-1,x), gdzie x należy od 0 do E)

Time: mamy O(nE) podproblemów, gdzie przy każdym musimy wykonać stałą ilość pracy, więc złożoność końcowa, to O(nE)
Warto zauważyć, że do punktu j można teleportować się z wielu planet, ale ich liczebność to maksymalnie n, więc
amortyzuje nam się koszt teleportu do stałego

"""

def planets( D, C, T, E ):
    n = len(D)
    dp = [[inf if i != 0 else b*C[0] for b in range(E+1)] for i in range(n)]
    t = [[] for i in range(n)]
    for i in range(n):
        if T[i][0] != i:
            t[T[i][0]].append([i,T[i][1]])
    for i in range(1,n):
        for b in range(E+1):
            if b == 0: # teleportuje się
                for j in range(len(t[i])):
                    a, p = t[i][j]
                    dp[i][b] = min(dp[i][b], dp[a][0] + p)
            else:#dotankowywuje
                dp[i][b] = min(dp[i][b], dp[i][b - 1] + C[i])
            if D[i]-D[i-1]+b <= E:# przylatuje z poprzedniej
                dp[i][b] = min(dp[i][b],dp[i-1][b+D[i]-D[i-1]])

    a = min(dp[n-1])
    return a

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
