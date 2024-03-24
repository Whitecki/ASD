def bowling(T):
    n = len(T)
    DP = [-1 for _ in range(n)]
    DP[0], DP[1] = max(0,T[0]), max(0,T[0], T[0]*T[1]) # Base Case
    for i in range(2,n): #Topological order
        DP[i] = max(DP[i-1],DP[i-1]+T[i],DP[i-2]+T[i]*T[i-1]) #Relate
    return DP[n-1] # original problem

