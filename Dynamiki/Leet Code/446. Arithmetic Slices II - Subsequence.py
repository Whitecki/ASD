"""
 Preprocessing: odejmuje każdą wartość o większym indeksie j od wartości o mniejszym indeksie i. Zapisuje wynik w słowniku
 jako dict[(i,T[j]-T[i])] = 1, jeśli już istnieje taki klucz, to zwiększam go o jeden.

 Algorytm: Dla każdego indeksu j w tablicy, iteruje po wszystkich mniejszych indeksach i. Sprawdzam czy istnieje w słowniku
 klucz równy (i,T[j] - T[i]). Jeśli istnieje taki klucz, to oznacza, że możemy stowrzyć nowy


 Niestety nie moge używać na egzaminie obsługi wyjątków, więc robię następne zadanie
"""