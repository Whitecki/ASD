from math import inf


# # partition problem function to
# # calculate sum between two indices
# # in array
# # funkcja licząca sume wartości podciągu spójnego od frm do to
#
# def sum(arr, frm, to):
#     total = 0;
#     for i in range(frm, to + 1):
#         total += arr[i]
#     return total
#
#
# # for n boards and k partitions
# def partition(arr, n, k):
#     # warunki końcowe, dla żadnego podziału i tablicy złożonej z jednego elementu
#     if k == 1:  # one partition
#         return sum(arr, 0, n - 1)
#     if n == 1:  # one board
#         return arr[0]
#     best = -inf
#
#     # find minimum of all possible
#     # maximum k-1 partitions to
#     # the left of arr[i], with i
#     # elements, put k-1 th divider
#     # between arr[i-1] & arr[i] to
#     # get k-th partition
#     for i in range(1, n + 1): # iterujemy po całej tablicy
#         # szukamy najmniejszego elementu z best i maxa
#         #max to większa wartość z sumy od itego do końca i rekurencyjnego wywołania podziału o jeden wcześniej
#
#         best = max(best,
#                    min(partition(arr, i, k - 1),
#                        sum(arr, i, n - 1)))
#     return best
#
#
# # Driver Code
# arr = [10, 20, 60, 50, 30, 40]
# n = len(arr)
# k = 3
# print(partition(arr, n, k))
#
# # This code is contributed
# # by sahilshelangia


# A DP based Python3 program for
# painter's partition problem

# function to calculate sum between
# two indices in list


# bottom up tabular dp
def findMax(arr, n, k):
    # initialize table
    dp = [[0 for i in range(n + 1)]
          for j in range(k + 1)]

    sum = [0 for _ in range(n + 1)]

    # k=1
    for i in range(1, n + 1):
        sum[i] = sum[i - 1] + arr[i - 1]

    for i in range(1, n + 1):
        dp[1][i] = sum[i]

    # n=1
    for i in range(1, k + 1):
        dp[i][1] = arr[0]

    # 2 to k partitions
    for i in range(2, k + 1):  # 2 to n boards
        for j in range(2, n + 1):

            # track minimum
            best = -inf

            # i-1 th separator before position arr[p=1..j]
            for p in range(1, j + 1):
                best = max(best, min(dp[i - 1][p], sum[j] - sum[p]))

            dp[i][j] = best

    # required
    return dp[k][n]


# # Driver Code
# arr = [10, 20, 60, 50, 30, 40]
# n = len(arr)
# k = 3
# print(findMax(arr, n, k))


# teraz ja :3

# Rozważmy ciąg (a0, . . . , an−1) liczb naturalnych. Załóżmy, że został podzielony
# na k spójnych podciągów: (a0, . . . , a`1
# ), (a`1+1, . . . , a`2
# ), . . . , (a`k−1+1, . . . , an−1). Przez wartość i-go podciągu
# rozumiemy sumę jego elementów a przez najgorszy podciąg rozumiemy podciąg o najmniejszej wartości
# (rozstrzygając remisy w dowolny sposób). Wartością podziału jest wartość jego najgorszego podciągu. Zadanie
# polega na znalezienie podziału ciągu (a0, . . . , an−1) o maksymalnej wartości.


# def śmieszna_nazwa(T, podziały):
#     n = len(T)
#     DP = [[0 for _ in range(n + 1)] for _ in range(podziały + 1)]
#
#     suma = [0 for i in range(n + 1)]
#
#     for i in range(1, n + 1):
#         suma[i] = T[i - 1] + suma[i - 1]
#
#     for i in range(1, podziały + 1):
#         DP[i][1] = T[0]
#
#     DP[1] = suma
#
#     for i in range(2, podziały + 1):
#         for j in range(2, n + 1):
#
#             nwm = - inf
#
#             for p in range(1, j + 1):
#                 sum = suma[j] - suma[p]
#                 niewiedza = DP[i - 1][p]
#
#                 nwm = max(nwm, min(suma[j] - suma[p], DP[i - 1][p]))
#
#             DP[i][j] = nwm
#
#     return DP[podziały][n]


# arr = [1, 2, 3, 4, 6, 15, 8, 7]
# k = 4
# print(śmieszna_nazwa(arr,k))
#

# teraz już serio ja sam

# Rozważmy ciąg (a0, . . . , an−1) liczb naturalnych. Załóżmy, że został podzielony
# na k spójnych podciągów: (a0, . . . , a`1
# ), (a`1+1, . . . , a`2
# ), . . . , (a`k−1+1, . . . , an−1). Przez wartość i-go podciągu
# rozumiemy sumę jego elementów a przez najgorszy podciąg rozumiemy podciąg o najmniejszej wartości
# (rozstrzygając remisy w dowolny sposób). Wartością podziału jest wartość jego najgorszego podciągu. Zadanie
# polega na znalezienie podziału ciągu (a0, . . . , an−1) o maksymalnej wartości.
from math import inf


def kurwa_w_końcu_to_umiem(T, grupki):
    n = len(T)
    DP = [[0 for i in range(n)] for i in range(grupki)]

    for i in range(grupki):
        DP[i][0] = T[0]

    suma = [0 for _ in range(n + 1)]

    for i in range(1, n + 1):
        suma[i] = T[i - 1] + suma[i - 1]

    DP[0] = suma[1:n+1]
    print(DP)
    for ilość_grupek in range(1, grupki):
        for wziąłem_tyle_liczb in range(1, n):
            posukiwana_wartość = -inf

            for podział in range(wziąłem_tyle_liczb):
                c = ilość_grupek - 1
                a = DP[ilość_grupek - 1][podział]
                b = suma[wziąłem_tyle_liczb] - suma[podział]
                posukiwana_wartość = max(posukiwana_wartość,
                                         min((suma[wziąłem_tyle_liczb] - suma[podział]), DP[ilość_grupek - 1][podział]))

            DP[ilość_grupek][wziąłem_tyle_liczb] = posukiwana_wartość
    print(DP)
    return DP[grupki - 1][n - 1]


arr = [1, 2, 3, 4, 6, 15, 8, 7]
k = 4
print(kurwa_w_końcu_to_umiem(arr, k))


# kurwa nwm
# jebać to
# nie jestem taki zjaebisty
# ale inni też nie są
# może nawet mniej :3