from zad5ktesty import runtests
from queue import Queue

def garek ( T ):
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
        if czy_ja:  # biorę większą wartość z opcji: biorę lewą monete i daje oponentowi ruch, lub biorę prawą i oponent
            dp_me[start][stop] = max(T[start] + dp_you[start - 1][stop], T[stop] + dp_you[start][stop + 1])
        else:
            dp_you[start][stop] = min(dp_me[start - 1][stop], dp_me[start][stop + 1])

    return dp_me[n - 1][0]

runtests ( garek )