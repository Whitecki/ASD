# Algorytm o złożoności O(k), niestety ma dość dużą stałą, wynoszącą 8^5 (32 768) :)))
def wyprawa_krzyzowa(x_start, y_start, k_ruchów,x_koniec,y_koniec):
    szachownica_1 = [[[False,0] for _ in range(8)] for _ in range(8)]
    szachownica_2 = [[[False,0] for _ in range(8)] for _ in range(8)]
    szachownica_1[y_start][x_start][0], szachownica_1[y_start][x_start][1] = True, 1
    for k in range(k_ruchów + 1):
        if k % 2 == 0:
            szachownica_2 = [[[False,0] for _ in range(8)] for _ in range(8)]
        else:
            szachownica_1 = [[[False,0] for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if (k % 2 == 0 and szachownica_1[i][j][0]) or (k % 2 == 1 and szachownica_2[i][j][0]):
                    for x, y in [[1, 2], [1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1], [-1, 2], [-1, -2]]:
                        if -1 < y + i < 8 and -1 < x + j < 8:
                            if k % 2 == 1:
                                szachownica_1[i + y][j + x][0] = True
                                szachownica_1[i + y][j + x][1] += szachownica_2[i][j][1]
                            else:
                                szachownica_2[i + y][j + x][0] = True
                                szachownica_2[i + y][j + x][1] += szachownica_1[i][j][1]
    if k_ruchów % 2 == 0:
        return szachownica_1[y_koniec][x_koniec][1]
    return szachownica_2[y_koniec][x_koniec][1]

print(wyprawa_krzyzowa(3,4,2,0,1))