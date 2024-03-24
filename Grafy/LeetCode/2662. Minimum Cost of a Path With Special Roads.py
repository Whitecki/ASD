"""
Zamieniamy listę krawędzi na listę sąsiedztwa. Przydatny tu będzie słownik
Prowadzimy od startowego wierzchołka do każdego innego krawędź, w tym do końcowego.
Waga każdej krawędzi jest dodatnia, więc można użyć dijkstry.
"""

def minimumCost(start, target,specialRoads):
    G = []
    dict = {}
    for x1,y1,x2,y2,w in specialRoads:


