from math import inf

def strings(A,B):
    a,b = len(A),len(B)
    # Na początku musimy znaleźć optymalną podstrukturę. Spróbuję na początek wziąć suffixy obu wyrazów.
    # subproblems: najmniejsza ilość zmian w wyrazach A[:i] i B[:j]
    dp = [[inf for _ in range(a+1)] for _ in range(b+1)]

    #Base case: 1) pusty wyraz A i pusty wyraz, nie wymagają zmian, natomiast jesli tylko jeden z wyrazów jest pusty, to
    # ilość zmian jest równa długości tego niepustego
    dp[0][0] = 0
    for i in range(a+1):
        dp[0][i] = i
    for i in range(b+1):
        dp[i][0] = i

    # topological order: z rekurencyjnego zapisu funkcji, wynika że aby rozwiązać podproblem dp[j][i], potrzebuje
    # podproblemów o mniejszych/równych wartościach j,i
    for j in range(1,b+1):
        for i in range(1,a+1):

            if A[i-1] == B[j-1]: # jeżeli literka jest taka sama, to biorę wartość bez tych dwóch literek
                dp[j][i] = dp[j-1][i-1]
            else:
                dp[j][i] = min(dp[j-1][i],dp[j][i-1],dp[j-1][i-1]) + 1 # usuwam lub dodaje lub zaminiam

    return dp[b][a]

A = "alibaba"
B = "babcia"
print(strings(A,B))