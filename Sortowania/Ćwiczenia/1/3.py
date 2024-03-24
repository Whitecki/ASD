#T posortowana tablica liczb x = liczba, sprawdź czy istnieje T[j] - T[i] = x
#jeden idx goni drugi
#dowód poprawności: jeśli istnieje rozwiązanie optymalne, to istnieje taki indeks i oraz j który spęłniają
# warunek T[j] - T[i] = x. Jeżeli idziemy idx k, m w prawo to jeśli idx k trafi na pole i, to wtedy m bedzie musiał
# trafić potem trafić na j
def f(T,x):
    i = 0
    n = len(T)
    j = n - 1
    while j < n:
        if T[j] - T[i] < x:

