# wydawało mi się, że gdyby reprezentacja grafu była normalna, to można by było zrobić VlogV
# odechciało mi się to wgl robić przez to
#Napisze więc sam pomysł: zamieniam reprezentacje grafu na listy sąsiedztwa
#na każdym zapisuje wartość przypisaną do danego wierzchołka i dodaje, jeśli zwiększy to wartość wierzchołka inne do których
# ma bezpośrednią krawędź
# 2 pomysł to posortować tablicę vals i dodawać wartości które pod nią lezą do wszystkich wierzchołków
def maxStarSum(vals, edges, k):


    left = [k ]