# Dana jest posortowana tablica A[1...n] oraz liczba x. Proszę napisać program, który stwierdza czy istnieją indeksy
# i oraz j takie, że A[i] + A[j] = x

# Rozwiązanie: 2 wskaźnikami ustawione na krańcach tablicy, przesuwamy w prawo, by zwiększyć sumę, gdy jest ona mniejsza od x
#analogicznie robimy przesuwając w lewo. W taki sposób jesteśmy w stanie sprawdzić każdą sumę

def pointers(A,x):
    n = len(A)
    a = 0
    b = n - 1
    while b > a:
        if A[a] + A[b] == x:
            return a,b
        elif A[a] + A[b] > x:
            b -= 1
        elif A[a] + A[b] < x:
            a += 1
    return False




