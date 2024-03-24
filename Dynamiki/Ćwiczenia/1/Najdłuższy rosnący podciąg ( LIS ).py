def LIS(T):
    n = len(T)
    T = [(T[i],i) for i in range(n)]
    sorted(T)
    dp = [1 for _ in range(n)]
    for i in range(1,n):
        pass