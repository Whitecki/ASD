# podejście w którym zauważam, że gra ma sumę zerową
def I_want_more(T: "array with contiguous subsequence of coins"):
    n = len(T)
    # preprocesiing: tworze tablice, która w O(1) odpowiada jaka kaska jest w sumie pomiędzy indeksami i oraz j
    suma = [T[0] if i == 0 else T[i] + T[i-1] for i in range(n)]
    # basic case: jeśli mam jedną monete do wzięcia, to lepiej jest ją wziąć
    raise NotImplemented

# Second solution uses subproblem expansion: add subproblems for when you move next

from queue import Queue


def I_want_more_and_more(T):
    n = len(T)
    # subproblems: maksymalna wartość kaski jaką mogę zgarnąć przy ruchu jednego z graczy, gdy na stole pozostał ciąg monet od i do j
    # Base case: jeśli została jedna moneta i jest moja kolej to ją biore, inaczej nic nie zyskuje
    dp_me = [[T[i] if i == j else 0 for i in range(n)] for j in range(n)]
    dp_you = [[0 for _ in range(n)] for _ in range(n)]

    # topological order: wkładam do kolejki, bo zabawa na idx, by spełnić warunek "każda komórka musi mieć wartość
    # powyżej i na prawo" jest zabawą dość nudna

    Q = Queue()
    for i in range(1, n):
        for j in range(n - i):
            Q.put((j + i, j, True))
            Q.put((j + i, j, False))

    while not Q.empty():
        start, stop, czy_ja = Q.get()
        # jeżeli jest moja kolej, to biorę wartość i dodaje
        if czy_ja: #biorę większą wartość z opcji: biorę lewą monete i daje oponentowi ruch, lub biorę prawą i oponent
            dp_me[start][stop] = max(T[start] + dp_you[start - 1][stop], T[stop] + dp_you[start][stop + 1])
        else:
            dp_you[start][stop] = min(dp_me[start - 1][stop], dp_me[start][stop + 1])

    return dp_me[n - 1][0]


T = [140,5, 10, 100, 25,30]

print(I_want_more_and_more(T))
