from zad7testy import runtests


def maze(L):
    n = len(L)
    # [wejście od lewej, od góry, od dołu]
    Graf = [[[0, 0, 0] for j in range(n)] for _ in range(n)]
    i = 0
    while i < n and L[i][0] != "#":
        Graf[i][1][0] = i + 1
        i += 1
    for wiersz in range(1, n - 1):
        Graf[0][wiersz][1] = Graf[0][wiersz][0]
        # od góry do dołu sprawdzam
        for kolumna in range(1, n):
            # jeżeli nie jest to kratka #
            if L[kolumna][wiersz] != "#" and (Graf[kolumna][wiersz][0] or Graf[kolumna - 1][wiersz][1]):
                # z góry biorę
                Graf[kolumna][wiersz][1] = max(Graf[kolumna - 1][wiersz][1] + 1, Graf[kolumna][wiersz][0])
        # od dołu do góry lecę
        Graf[n - 1][wiersz][2] = Graf[n - 1][wiersz][0]
        for kolumna in range(n - 2, -1, -1):
            # jeżeli nie jest to kratka #
            if L[kolumna][wiersz] != "#" and (Graf[kolumna + 1][wiersz][2] or Graf[kolumna][wiersz][0]):
                # z dołu biorę
                Graf[kolumna][wiersz][2] = max(Graf[kolumna + 1][wiersz][2] + 1, Graf[kolumna][wiersz][0])
        # przekazuje w prawo
        if wiersz != n - 1:
            for kolumna in range(n):
                if L[kolumna][wiersz] != "#" and (
                        Graf[kolumna][wiersz][0] or Graf[kolumna][wiersz][1] or Graf[kolumna][wiersz][2]) and \
                        L[kolumna][wiersz + 1] != "#":
                    Graf[kolumna][wiersz + 1][0] = max(Graf[kolumna][wiersz][2] + 1, Graf[kolumna][wiersz + 1][0],
                                                       Graf[kolumna][wiersz][1] + 1)

    Graf[0][n - 1][1] = Graf[0][n - 1][0]
    # od góry do dołu sprawdzam
    for kolumna in range(1, n):
        # jeżeli nie jest to kratka #
        if L[kolumna][n - 1] != "#" and (Graf[kolumna][n - 1][0] or Graf[kolumna - 1][n - 1][1]):
            # z góry biorę
            Graf[kolumna][n - 1][1] = max(Graf[kolumna - 1][n - 1][1] + 1, Graf[kolumna][n - 1][0])
    result = max(Graf[n - 1][n - 1][1], Graf[n - 1][n - 1][0])
    if result:
        return result
    return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
