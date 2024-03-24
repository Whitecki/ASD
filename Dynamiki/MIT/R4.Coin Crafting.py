#trochę problem plecakowy here
from math import inf
def Krasnoludy(P:"cena sprzedaży i-tego przedmiotu",M:"ilość monet potrzebnych do przetopienia w i-ty przedmiotu"):
    n = len(P)
    #max ilość kaski jaką złodziej zarobi przy sprzedaniu niektórych z i pierwszych przedmiotów i przemieleniu j monet
    #Base case: jeśli mam 0 monet do przemielenia, albo 0 przedmiotów wziąłem, to wiadomo że mam 0 kaski
    dp = [[0 if (i==0 or j == 0) else -inf for j in range(n+1)] for i in range(n+1)]
    #kolejność topologiczna
    for i in range(1,n+1):
        for j in range(1,n+1):
            # jeśli się jedna więcej moneta/przedmiot zwiększa ilość kaski możliwej do zgarniecia, to bierzemy
            if j - M[i-1] < 0:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i-1][j-M[i-1]] + P[i-1])
    #zwracam tablice idx monet które trzeba przemielić :)
    result = []
    i,j = n,n
    while i > 0 and j > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1
        else:
            result.append(i-1)
            i -= 1
            j-= M[i]
    return result

P = [2,6,3,5,8,7,16]
M = [1,2,1,2,4,3,7]
print(Krasnoludy(P,M))