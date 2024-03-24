from math import inf
def serio_trudne_zadanie(A,m):
    n = len(A)
    dp = [[[[False for l3 in range(m+1)] for l2 in range(m+1)] for l1 in range(m+1)] for i in range(n)]
    dp[0][A[0]][0][0], dp[0][0][A[0]][0], dp[0][0][A[0]][0], dp[0][0][0][0] = True, True, True, True
    for i in range(1,n):
        for l1 in range(m+1):
            for l2 in range(m+1):
                for l3 in range(m+1):
                    a,b,c = False, False, False
                    if l1 - A[i] > -1:
                        a = dp[i-1][l1-A[i]][l2][l3]
                    if l2 - A[i] > -1:
                        b = dp[i - 1][l1 - A[i]][l2][l3]
                    if l3 - A[i] > -1:
                        c = dp[i - 1][l1 - A[i]][l2][l3]
                    dp[i][l1][l2][l3] = (dp[i-1][l1-A[i]][l2][l3] or dp[i-1][l1][l2-A[i]][l3] or dp[i-1][l1][l2][l3-A[i]] or dp[i-1][l1][l2][l3])
    min_max = inf
    for l1 in range(m + 1):
        for l2 in range(m + 1):
            for l3 in range(m + 1):
                if dp[-1][l1][l2][l3]:
                    min_max = min(max(l1,l2,l3,m-l1-l2-l3),min_max)
    return min_max

A = [1,8,7,5,4,3]
print(serio_trudne_zadanie(A,sum(A)))