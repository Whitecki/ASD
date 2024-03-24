# Dane jest słowo będące tablicą n znaków z alfabetu E, o rozmiarze |E|. Dana jest również liczba k. Długość słowa
# wynosi co najmniej |E|^k. Zaproponuj algorytm, który zwróci najczęściej powtarzający się w tym słowie spójny podciąg
# o długości k. Algorytm ma działać w czasie O(n), wykorzystywać O(1) pamięci. Ponadto zawartość tablicy po wykonaniu
# algorytmu powinna pozostać niezmieniona.
#
# Hint: zadanie jest trudne :)

'''idea 1: Robimy tablice E * k, która będzie reprezentować, każde możliwe słowo. Traktujemy każdą litere jako liczbę z
zakresu 0 do E-1. Robimy tablice 2D E * k, która będzie reprezentować, każde możliwe słowo.
Następnie idziemy “oknem przesuwnym” rozmiaru k. interpretujemy dane słowo jako ciąg liczb, za pomocą których
dodajemy 1 do odpowiedniego koszyka.'''


''' idea 2:
Co gdyby alfabet potraktować jako cyfry systemu liczbowego?
No więc tak:
Każdy podciąg o długości k to liczba zapisana w systemie o podstawie E, z zakresu 0 do E^k - 1. Możemy wykorzystać
indeksy słowa jako miejsca na trzymanie liczników ich wystąpień, w ten sposób “omijamy” ograniczenie O(1) pamięci 
(trzeba je będzie potem przywrócić do stanu pierwotnego, ale tym się zajmiemy później). Zauważamy, że litery to cyfry
od 0 do E-1. W każdym indeksie chcemy trzymać więcej count + litera. Problem: jak mieć dostęp tylko do licznika lub
tylko do litery? Rozwiązanie: trzymać count * E + litera, na koniec wystarczy wtedy zrobić %E i otrzymujemy samą
literę. Dostęp do licznika otrzymujemy za to przez / E.

Samo zliczanie wygląda następująco: idziemy “oknem przesuwnym” rozmiaru k i patrzymy na kolejne podciągi (w Pythonie
łatwo wyciąć coś takiego slicingiem). Interpretując taki podciąg jako liczbę, inkrementujemy odpowiedni licznik (taki
0podciąg to po prostu k-pozycyjna liczba w systemie o podstawie E, patrz WDI).
'''