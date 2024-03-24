#T = [[długosc, szerokosc, wysokosc] for_ in range(n)]
def buildings(T):

    n = len(T)
    #sorted_T = [pole powierzchni, wysokość, dwa pozostałe wymiary, idx w orginalnej tablicy]
    sorted_T = [[T[i//3][i%3 + 1]*T[i//3][i%3 + 2],T[i//3][i%3],T[i//3][i%3+1],T[i//3][i%3+2], i//3] for i in range(3*n)]
    sorted_T = sorted(T,key = lambda x: x[0]) #O(nlogn)

    # is_here[i][j] - czy już został użyty klocek i-ty w wierzy, której najwyższym klockiem jest j-ty
    is_here = [[False for _ in range(3*n)] for _ in range(n)] #O(n^2)

    #subproblems: najwyższa wierza do i-tego wyrazu, z użyciem tego wierzchołka
    dp = [0 for _ in range(n+1)]

    for i in range(1,3*n+1): #O(n^2)
        for j in range(i-1,0,-1):
            # jeżeli nowy klocek ma obie mniejsze krawędzie i nie został juz wcześniej użyty
            if not is_here[i-1][j] and ((T[i-1][2] < T[j-1][2] and T[i-1][3] < T[j-1][3]) or (T[i-1][2] < T[j-1][3] and T[i-1][3] < T[j-1][2])):
                dp[i] = dp[j] + sorted_T[i-1][1]
                is_here[i-1][j] = True
                break
            dp[i] = sorted_T[i-1][1]
    return dp[n]

T = []