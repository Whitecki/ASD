from zad3ktesty import runtests
from math import inf


# time: O(nk), niestety może sie skwadracić, bo k zawiera się w przedziale (1,n). Można zrobić O(nlogk), jeśli za pomocą
# kopca byśmy szukali najmniejszego elementu w logk, przy (n-k) iteracjach.
def ksuma(T, k):
    # dp(i)-najmniejsza suma elementów tablicy T[:i], jeśli w każdej podtablic T[i:i+k] jest chociaż jeden wzięty element
    n = len(T)
    dp = [T[i] if i < k else inf for i in range(n + 1)]
    # last_k = [T[i] for i in range(k)]
    for i in range(k, n):
        for j in range(i - 1, i - k - 1, -1):
            dp[i] = min(dp[j]+T[i], dp[i])
    result = inf
    for i in range(n-1,n-k-1,-1):
        result = min(result,dp[i])
    return result


runtests(ksuma)
