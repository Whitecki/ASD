# wstawianie do kopca binarnego

class Heap:
    def __init__(self,n):
        self.T = [0 for _ in range(0)]
        self.size = 0 # indeks ostatniego elementu

def insert(H,x):
    if H.size == 0:
        H.T[0] = x
        H.size += 1
        return
    i = H.size
    p = (H.size - 2) // 2
    H.T[H.size] = x
    H.size += 1
    while p >= 0:
        if H.T[p] < H.T[i]:
            H.T[p], H.T[i] = H.T[i], H.T[p]
        else: break
        i = p
        p = (p-1)//2