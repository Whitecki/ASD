# # Zadanie 7. (wędrówka po szachownicy) Dana jest szachownica A o wymiarach n × n. Szachownica
# # zawiera liczby wymierne. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół”
# # oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
# # znajdujący trasę o minimalnym koszcie

from math import inf


def dziekan(T):
    n = len(T)
    DP = [[inf for _ in range(n)] for _ in range(n)]

    # początkową i końcową wartość i tak musimy odwiedzić więc ich koszt to zera
    DP[0][0] = 0
    DP[n - 1][n - 1] = 0

    # na prawo od początkowego pkt, można iść tylko w jeden sposób
    for i in range(1, n):
        DP[0][i] = (DP[0][i - 1] + T[0][i])

    # w dół od początkowego pkt, można iść tylko w jeden sposób
    for i in range(1, n):
        DP[i][0] = (DP[i-1][0] + T[i][0])

    # idziemy do danej komórki z góry lub z dółu zależnie od tego która ścieżka ma mniejszy koszt
    for i in range(1, n):
        for j in range(1, n):
            DP[i][j] = min(DP[i - 1][j], DP[i][j - 1]) + T[i][j]

    # mamy już minimalny koszt dojścia do końca, więc wracamy wybierając
    # pola o jak najmniejszej wartości i zapisując którędy idziemy

    i = n - 1
    j = n - 1
    wynik = [(n-1,n-1)]

    while j >= 1 and i >= 1:

        # idziemy w lewo, bo tam taniej (#ekonomia wszędzie)
        if DP[i][j - 1] < DP[i - 1][j]:
            wynik.append((i, j - 1))
            j -= 1

        else:
            wynik.append((i - 1, j))
            i -= 1

    while j != 0:
        wynik.append((1, j))
        j -= 1

    while i != 0:
        wynik.append((i, 1))
        i -= 1

    return wynik,DP


A = [[1, 3, 5, 8],
     [4, 2, 1, 7],
     [4, 3, 2, 3],
     [5, 5, 5, 5]]


g, T = dziekan(A)
print(g)
print(T)
