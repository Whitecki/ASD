def tniemy_deche(val:"cena za deskę o długości l",L:"długość całej deski"):
    dp = [val[i] for i in range(L)]
    dp[1] = max(val[0]*2,val[1])
    for i in range(2,L):
        lewy = 0
        prawy = i-1
        while prawy >= lewy:
            dp[i] = max(dp[lewy] + dp[prawy],dp[i])
            prawy -= 1
            lewy += 1

    return dp[L-1]

val = [1,10,13,18,20,31,32]
L = 7

print(tniemy_deche(val,L))
