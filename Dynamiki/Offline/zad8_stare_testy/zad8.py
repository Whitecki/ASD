from zad8testy import runtests


from queue import Queue
#Time: O(nm)

def plan(T):
    n = len(T)
    m = len(T[0])

    # preprocessing - zapisuje ile ropy jest na każdym polu. Działa to trochę jak BFS, którego puszczam z każdego pola
    #na którym stanie nasz podróżnik. Jeżeli ropa wypływa na powierzchnie w dówch miejscach przypisuje ją do wcześniejszego
    #Jeżli ropy jest więcej niz potrzeba by dotrzeć do końca, to biorę tylko tyle ile się zużyje. Time: O(nm)
    ile_ropy = [0 for _ in range(m)]
    Q = Queue()
    for i in range(m):
        if T[0][i]:
            suma = 0
            Q.put((0, i))
            while not Q.empty():
                y, x = Q.get()
                if T[y][x]:
                    suma += T[y][x]
                    T[y][x] = 0
                    for j, ii in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                        if 0 <= j + y < n:
                            if 0 <= ii + x < m:
                                if T[j + y][ii + x]:
                                    Q.put((j + y, ii + x))
            if m - i < suma + 1:
                ile_ropy[i] = m - i - 1
            else:
                ile_ropy[i] = suma

    # Jeśli mam paliwo, to idę do przodu. Zapamiętuje przy okazji jaką najwiekszą ilość ropy widziałem od ostatniego tankowania.
    # Jeżeli braknie paliwa, to tankuje największym złożem, Które nie zostało jeszcze zużyte. Jeśli nie wiem, które złoże
    # jest największym niezużytym, to go szukam. Musi być ono mniejsze od poprzedniego największego złoża. Zaczynam
    # sprawdzanie o jedną pojemność mniej, aż znajdę nowe najw. Biorąc pod uwagę, że cofam się maksymalnie o wartość, którą
    # wcześniej pojechałem do przodu, to wydaje mi się, że mogę maksymalnie zrobić 2m operacji tutaj. Time: O(m)
    paliwo = ile_ropy[0]
    tu_jestem = 1
    max_ilosc_paliwa = 0
    ile_razy_tankowalem = 1
    bak = [0 for _ in range(m)]  # ile pól o pojemności i mamy jeszcze niezużytych
    while tu_jestem < m:
        while paliwo > 0 and tu_jestem != m- 1:
            paliwo -= 1
            # zapisuje gdzie jest najwieksze złoże
            if ile_ropy[tu_jestem] > max_ilosc_paliwa:
                max_ilosc_paliwa = ile_ropy[tu_jestem]
            bak[ile_ropy[tu_jestem]] += 1

            if paliwo > 0:
                tu_jestem += 1

        # dotarłem do końca
        if tu_jestem == m - 1:
            return ile_razy_tankowalem

        # brakło paliwa
        while not bak[max_ilosc_paliwa]:
            max_ilosc_paliwa -= 1
        paliwo += max_ilosc_paliwa
        tu_jestem += 1
        ile_razy_tankowalem += 1
        bak[max_ilosc_paliwa] -= 1
    return ile_razy_tankowalem


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)


