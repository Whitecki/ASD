from math import inf


def Bankomat(kwota, monety):
    wykaz_konta = [inf for _ in range(kwota + 1)]
    wykaz_konta[0] = 0
    # biorę każdą kolejną monetę
    a = len(monety)
    for i in range(a):
        for j in range(kwota + 1 - monety[i]):
            # biorę minimum z: nie używam nowego nominału lub cofam się o ostatnie użycie tego nominału i dodaje 1
            wykaz_konta[j + monety[i]] = min(wykaz_konta[j + monety[i]], wykaz_konta[j] + 1)

    return wykaz_konta[kwota]

kwota = 18
monety = [1,2,5,10]
wynik = Bankomat(kwota, monety)
print((wynik))
