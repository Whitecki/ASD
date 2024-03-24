# Obraz jest reprezentowany przez dwuwymiarową tablicę liczb całkowitych,
# z których każda reprezentuje wartość piksela obrazu.
#
# Biorąc pod uwagę współrzędne (sr, sc) reprezentujące początkowy piksel (wiersz i kolumnę) wypełnienia powodziowego
# oraz wartość piksela newColor, „wypełnij” obraz.
#
# Aby wykonać „wypełnienie zalewowe”, należy wziąć pod uwagę piksel początkowy plus wszystkie piksele połączone
# 4-kierunkowo z pikselem początkowym tego samego koloru co piksel początkowy oraz wszystkie piksele połączone
# 4-kierunkowo z tymi pikselami (również o tym samym kolorze co piksel początkowy) początkowy piksel) i tak dalej.
# Zamień kolor wszystkich wyżej wymienionych pikseli na newColor.

'''działa :))). DFS za prosty by tłumaczyć'''

def floodFill(self, G, i, j, newColor):
    I, J = len(G), len(G[0])
    visited = [[False for _ in range(J)] for _ in range(I)]
    result = []

    def dfsVisit(G, i, j, visited, I, J, result):
        visited[i][j] = True
        result.append((i, j))

        for el in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if -1 < i + el[0] < I and -1 < j + el[1] < J and not visited[el[0] + i][el[1] + j] and G[el[0] + i][
                el[1] + j] == G[i][j]:
                dfsVisit(G, i + el[0], j + el[1], visited, I, J, result)

    dfsVisit(G, i, j, visited, I, J, result)
    for (i, j) in result:
        G[i][j] = newColor
    return G


image = [[1,1,1],[1,1,0],[1,0,1]]
newColor = 2
floodFill(image,0,0,newColor)
print(image)