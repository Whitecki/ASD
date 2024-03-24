"""
Tworze listę sąsiedztwa
Znajduje 3 największych sąsiadów dla każdego wierzchołka, czyli liniowo przechodze po każdej liście sąsiedztwa. O(E)
Tworze macierz sąsiedztwa, aby wiedzieć w O(1), czy są ze sobą połączone dwa wierzchołki. O(V**2)
Następnie wybieram 2 wierzchołki O(V**2)
Łącze je z największymi możliwymi wierzchołkami O(1)
Time: O(V**2)
"""
def helper(i,j,G):
    maxi = 0
    pass
    return maxi

def maximumScore(A, E):
    n = len(A)
    G = [[] for _ in range(n)]
    lenn = [0 for _ in range(n)]
    for x, y in E:
        G[x].append(y)
        G[y].append(x)
        lenn[x] += 1
        lenn[y] += 1

    for i in range(n):
        vala, valb, valc = G[i][0], G[i][1], G[i][2]
        a, b, c = 0, 1, 2
        for j in range(3, lenn[i]):
            if min(valb, valc, vala) > G[i][j]:
                if vala > G[i][j] or valc > G[i][j]:
                    if vala > G[i][j]:
                        vala = G[i][j]
                        a = j
                    else:
                        valc = G[i][j]
                        c = j
                else:
                    valb = G[i][j]
                    b = j
            G[i][a], G[i][b], G[i][c] = G[i][0], G[i][1], G[i][2]
            G[i][:2] = sorted(G[i][:2])

    MS = [[0 for _ in range(n)] for _ in range(n)]
    for x, y in E:
        MS[x][y] = 1
        MS[y][x] = 1

    A = [[A[i], i] for i in range(n)]
    A = sorted(A, key=lambda x: x[0])
    result = 0
    for i in range(n):
        for j in range(i + 1,n):
            if MS[i][j]:
                result = max(helper(i,j,G),result)
                # ifologia tutaj

    return result

