"""
Zadanie bardzo fajnego typu.
1. zliczam ile krawędzi wchodzi do każdego wierzchołka. Jeżeli wchodzi tylko jedna, to ten wierzchołek jest liściem.
2. Sprawdzam wysokość każdego wierzchołka, zdefiniowaną jako maksymalna wartość jego dzieci + 1. Liście mają wartość 1.
W taki sposób powstaje root. Zapamiętuje w każdym wierzchołku, która krawędź prowadzi do wyższego wierzchołek.
3. Z każdej monety oznaczam wierzchołek o 2 wysokości wyżej jako obowiązkowy do odwiedzenia.
4. Zliczam odległości od oznaczonych wierzchołków do root-a, z uwzględnieniem niektórych wierzchołków.
"""

def collectTheCoins(coins, edges):
    pass