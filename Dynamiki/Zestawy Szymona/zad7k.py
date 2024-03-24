from zad7ktesty import runtests 
#taki trochę plecakowy
from queue import Queue

def ogrodnik (T, D, Z, L):
    n = len(Z)
    m = len(T)
    idx = 0
    for korzenie in D:
        Q = Queue()
        Q.put((0,korzenie))
        suma = 0
        while not Q.empty():
            y,x = Q.get()
            if T[y][x]:
                suma += T[y][x]
                T[y][x] = 0
                for j,i in [[1,0],[0,1],[-1,0],[0,-1]]:
                    if 0<i+y<m and 0<j+x<n and T[i+y][j+x]:
                        Q.put((y+i,x+j))
        D[idx] = suma
        idx+=1

    #dp(i,l) - max wartość owoców, jeśli mam l litrów wody i biore pod uwage pierwsze i drzewek

    dp = [[0 for _ in range(L+1)] for _ in range(n+1)]
    for i in range(1,L+1):
        for j in range(1,n+1):
            pass
    return

runtests( ogrodnik, all_tests=False )
