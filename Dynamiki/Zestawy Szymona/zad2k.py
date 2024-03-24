from zad2ktesty import runtests

"""
Algorytm: trywialny
Time: O(n**2), przy czym średnia to O(n)
"""


def palindrom(S):
    n = len(S)
    i = 0
    max_cnt = 0
    a,b = -1,-1
    # nieparzyste
    while i < n:
        j = i - 1
        k = i + 1
        cnt = 1
        while j > -1 and k < n and S[j] == S[k]:
            j -= 1
            k += 1
            cnt += 2
        if max_cnt < cnt:
            max_cnt = cnt
            a = j+1
            b = k -1
        k = i+1
        j = i
        cnt = 0
        while j > -1 and k < n and S[j] == S[k]:
            cnt += 2
            k += 1
            j -=1
        if max_cnt < cnt:
            max_cnt = cnt
            a = j + 1
            b = k - 1
        i+= 1

    return S[a:b+1]


runtests(palindrom)
