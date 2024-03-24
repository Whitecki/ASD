# Mamy daną tablice A z n liczbami naturalnymi. Proszę zaproponowac algorytm o złozoności O(n), który stwierdza, czy
#w tablicy ponad połowa elementów ma jednakową wartość. Lider ciągu :))

def lider(A):
    n = len(A)
    i,cnt,candidat = 0,0,"a"
    while i < n:
        if A[i] == candidat:
            cnt += 1
        else:
            if cnt != 0:
                cnt -= 1
            if cnt == 0:
                candidat = A[i]
                cnt = 1
    cnt = 0
    for i in range(n):
        if A[i] == candidat:
            cnt += 1

    if 2*cnt > n:
        return True
    return False