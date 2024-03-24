# Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności
# O(n), który stwierdza, czy istnieje liczba x (tzw. lider A), która występuje w A na ponad połowie pozycji.

# Rozwiązanie: najpierw szukamy kandydata na lidera ciągu. Iterujemy przez tablicę dodając jeden do cnt, jeżeli
#powtórzył się aktualny kandydat. Jeżeli cnt == 0, to zmieniamy kandydata. Następnie jeszcze raz przechodzimy przez tablicę,
#sprawdzając czy kandydat jest faktycznie liderem ciągu

def f(A):
    n = len(A)
    cnt = 1
    a = A[0]
    for i in range(1,n):
        if a == A[i]:
            cnt+=1
        else:
            cnt -= 1
            if cnt == 0:
                cnt = 0
                a = A[i]
    cnt = 0
    for i in range(n):
        if A[i] == a:
            cnt+= 1

    if cnt*2 > n:
        return True
    else:
        return False