class graph:
    def __init__(self):


def matrix(c,e):
    # ile jest oaz i tego drugiego
    n = 0
    for x,y in e:
        n = max(n,x,y)
    n += 1
    #
    czy_kropka = [True for _ in range(n)]
    ile_kropek = 0
    for el in c:
        czy_kropka[el] = False
    #sprawdzam czy oazy są bezpośrednio połączone
    for x,y in e:
        if czy_kropka[x] and czy_kropka[y]:
            



def check_mate(g,o):
    G = matrix(g,o)
    return

E = [(0, 1), (1, 2), (2, 3), (3, 5), (4, 5), (4, 7), (5, 9), (3, 9), (1, 7), (0, 7), (7, 10), (10, 11),
     (1, 6), (6, 8)]
C = [0, 2, 9, 4, 10, 6]