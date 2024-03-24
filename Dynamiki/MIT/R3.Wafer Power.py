
#reprezentacja T = [False, True, False, False, ...... i tak n razy False albo True]

def ale_duzo_kresek(T):
    n = len(T)
    #na idx pierwszym i drugim jest informacja, czy lewy i prawy koniec łuku są już połączone z jakąś kropką
    dp = [[0 for _ in range(n)]for _ in range(n)]
    for i in range(2,n): # długość łuku
        for j in range(n): # miejsce od którego zaczynam łuk
            dp[j%n][(j+i)%n] = dp[(j+1)%n][(j+i-1)%n]
            if (T[i] == False and T[j] == True) or (T[j] == False and T[i] == True) and abs(j%n - i%n) > 1:
                dp[j%n][(j+i)%n] += 1
            # mniejszy łuk
            for k in range(i):
                dp[j%n][(j + i) % n] = max(dp[j%n][(j+i)%n],dp[j%n][(j+k)%n] + dp[(j+1+k)%n][(j+i)%n])
    return dp[0][n-1]

T = [0,1,0,0,1,1,0,0,1,1,1,0,0,0,1]
print(ale_duzo_kresek(T))




            # wywali się bo przekręci się tablica :)))



