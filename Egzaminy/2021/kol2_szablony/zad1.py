from zad1testy import runtests
#O(pnlogn), parenty jeszcze trzeba dopisać
def binarry(poczatek, koniec, wartosc,T):
    if koniec == wartosc:
        return koniec
    while koniec - poczatek > 1:
        mid = (koniec+poczatek)//2
        if T[koniec][2] == wartosc:
            return koniec
        if T[mid][3] > wartosc:
            koniec = mid
        else:
            poczatek = mid
    if T[koniec][2] > wartosc:
        return -1

    return koniec

def select_buildings(T, p):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    sorted(T,key= lambda x: x[2])
    parent = [[-1 for _ in range(p)] for _ in range(n)]
    dp = [[0 for k in range(p)] for i in range(n+1)]
    #Base case: pierwszy domek
    for k in range(T[0][3],p+1):
        dp[0][k] = T[0][0]*(T[0][2]-T[0][1])
    for i in range(1,n):
        j = binarry(0,i-1,T[i][1],T)
        for k in range(T[i][3],p):
            dp[i][k] = max(dp[i - 1][k], dp[i][k - 1])
            if dp[j][k-T[i][3]] + T[i][0]*(T[i][2]-T[i][1]) > dp[i][k]:
                dp[i][k] = dp[j][k-T[i][3]] + T[i][0]*(T[i][2]-T[i][1])
                parent[i][k] = j
    return []

runtests( select_buildings ) 
