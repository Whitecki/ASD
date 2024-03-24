from zad1testy import runtests
from math import inf

def rect(D):
    """tu prosze wpisac wlasna implementacje"""
    n = len(D)
    max_x1, max_y1, min_x2, min_y2 = -inf, -inf, inf,inf
    idx_x1, idx_y1, idx_x2, idx_y2 = -1,-1,-1,-1
    for i in range(n):
        if max_x1 < D[i][0]:
            max_x1 = D[i][0]
            idx_x1 = i
        if max_y1 < D[i][1]:
            max_y1 = D[i][1]
            idx_y1 = i
        if min_x2 > D[i][2]:
            min_x2 = D[i][2]
            idx_x2 = i
        if min_y2 > D[i][3]:
            min_y2 = D[i][3]
            idx_y2 = i
    pole = 0
    idx = 0
    for j in [idx_x1,idx_x2,idx_y1,idx_y2]:
        max_x11, max_y11, min_x21, min_y21 = -inf, -inf, inf, inf
        idx_x11, idx_y11, idx_x21, idx_y21 = -1, -1, -1, -1
        for i in range(n):
            if j != i:
                if max_x11 < D[i][0]:
                    max_x11 = D[i][0]
                    idx_x11 = i
                if max_y11 < D[i][1]:
                    max_y11 = D[i][1]
                    idx_y11 = i
                if min_x21 > D[i][2]:
                    min_x21 = D[i][2]
                    idx_x21 = i
                if min_y21 > D[i][3]:
                    min_y21 = D[i][3]
                    idx_y21 = i
        if pole < (min_x21 - max_x11) * (min_y21 - max_y11):
            pole = (min_x21 - max_x11) * (min_y21 - max_y11)
            idx = j
    return idx

    
runtests( rect )


