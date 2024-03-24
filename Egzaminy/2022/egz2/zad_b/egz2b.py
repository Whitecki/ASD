from egz2btesty import runtests

# coś jest nie tak z testami. W teście nr. 2 testy wybierają pierwsze wyjście w 7 komnacie, pomimo że druga jest lepsza

def magic( C ):
    n = len(C)
    ile_tu_donioslem = [0 for _ in range(n)]
    visited = [False for _ in range(n)]
    visited[0] = True
    for i in range(n):
        if visited[i]:
            for a,el in C[i][1:4]:
                if ile_tu_donioslem[i] + C[i][0] >= a and el > i:
                    ile_tu_donioslem[el] = max(min(ile_tu_donioslem[i] + C[i][0] - a,ile_tu_donioslem[i]+10), ile_tu_donioslem[el])
                    visited[el] = True
    if ile_tu_donioslem[n-1] == 0:
        return -1
    return ile_tu_donioslem[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
