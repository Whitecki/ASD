# goal: tak postawić statki o rozmiarach 2x1, by jak najwięcej kaski zgarnąć

def statki(T: "tablica pionowa rozmiaru n o szerokości 2, na każdym polu jest wartość"):
    n = len(T)
    # subproblems: dp[i,j] największa wartość kaski możliwej do zgarnięcia od 0 do i lub j
    po_rowno = [0 for _ in range(n)]  # największa wartość, jeśli ostatni statek jest położony poziomo
    po_lewej_klade = [0 for _ in
                      range(n)]  # największa wartość, jeśli ostatnia łódka jest położona pionowo po lewej stronie
    po_prawej_klade = [0 for _ in
                       range(n)]  # największa wartość, jeśli ostatnia łódka jest położona pionowo po prawej stronie
    # base case: stawiam na polu o wymiarach 2x1 łódkę poziomo, jesli się to opłaca
    if T[0][0] + T[0][1] > 0:
        po_rowno[0] += T[0][0] + T[0][1]
    if T[1][0] + T[1][1] > 0:
        po_rowno[1] = po_rowno[0] + T[1][0] + T[1][1]
    if T[0][0] + T[1][0] > 0:
        po_lewej_klade[1] = T[0][0] + T[1][0]
    if T[0][1] + T[1][1] > 0:
        po_prawej_klade[1] = T[0][1] + T[1][1]

    # wiersz po wierszu dodajemy
    for i in range(2, n):
        # jeżeli się to opłaca, to stawiam poziomo statek
        po_rowno[i] = max(max(po_rowno[i - 1], po_lewej_klade[i - 1], po_prawej_klade[i - 1]) + T[i][0] + T[i][1],
                          po_rowno[i - 1])

        # jeśli położenie pionowo łódki po prawo, da wartość dodaną, to kładę ją
        po_prawej_klade[i] = max(
            max(po_rowno[i - 2], po_lewej_klade[i - 1], po_prawej_klade[i - 2]) + T[i][1] + T[i - 1][1],
            po_prawej_klade[i - 1])

        # jeśli położenie pionowo łódki po lewo, da wartość dodaną, to kładę ją
        po_lewej_klade[i] = max(
            max(po_lewej_klade[i - 2], po_prawej_klade[i - 1], po_rowno[i - 2]) + T[i][0] + T[i - 1][0],
            po_lewej_klade[i - 1])

    return max(po_rowno[n - 1], po_prawej_klade[n - 1], po_lewej_klade[n - 1])

T = [[7,7],
     [7,7],
     [0,0],
     [3,-10],
     [3,5],
     [-10,5],
     [-10,-5]]

print(statki(T))
