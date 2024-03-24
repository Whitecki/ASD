from egz1Atesty import runtests
from math import inf



def heapify(Heap, Gdzie_w_kopcu, i, n):
    l, r, max_idx = 2 * i + 1, 2 * i + 2, i

    if l < n and Heap[l][0] < Heap[max_idx][0]:
        max_idx = l
    if r < n and Heap[r][0] < Heap[max_idx][0]:
        max_idx = r

    if max_idx != i:
        Heap[i], Heap[max_idx] = Heap[max_idx], Heap[i]
        Gdzie_w_kopcu[Heap[i][1]], Gdzie_w_kopcu[Heap[max_idx][1]] = Gdzie_w_kopcu[Heap[max_idx][1]], Gdzie_w_kopcu[Heap[i][1]]
        heapify(Heap, Gdzie_w_kopcu, max_idx, n)


def heapify_up( Heap, Gdzie_w_kopcu, i):
    max_idx = (i - 1) // 2
    if max_idx > -1 and Heap[i][0] < Heap[max_idx][0]:
        Heap[i], Heap[max_idx] = Heap[max_idx], Heap[i]
        Gdzie_w_kopcu[Heap[i][1]], Gdzie_w_kopcu[Heap[max_idx][1]] = Gdzie_w_kopcu[Heap[max_idx][1]], Gdzie_w_kopcu[Heap[i][1]]
        return heapify_up(Heap,Gdzie_w_kopcu, max_idx)
    return i


def delete(Heap, Gdzie_w_kopcu, L, d):  # usuwam i-ty element
    Heap[d], Heap[L - 1] = Heap[L - 1], Heap[d]
    Heap[L-1] = (inf, Heap[L-1][1])
    Gdzie_w_kopcu[Heap[d][1]], Gdzie_w_kopcu[Heap[L - 1][1]] = Gdzie_w_kopcu[Heap[L - 1][1]], Gdzie_w_kopcu[Heap[d][1]]
    heapify(Heap, Gdzie_w_kopcu, heapify_up(Heap, Gdzie_w_kopcu, d), L)


def insert(val, Heap, Gdzie_w_kopcu, L, i):
    Heap[L - 1] = (val, Heap[L-1][1])
    heapify(Heap, Gdzie_w_kopcu, heapify_up(Heap, Gdzie_w_kopcu,L - 1), L)

def Dijkstra(a,G):
    n = len(G)
    Heap = [(inf, i) for i in range(n)]
    Heap[a],Heap[0] = Heap[0], (0,a)
    Gdzie_w_kopcu = [i for i in range(n)]
    Gdzie_w_kopcu[a], Gdzie_w_kopcu[0] = Gdzie_w_kopcu[0], Gdzie_w_kopcu[a]
    distance_a = [inf for i in range(n)]
    distance_a[a] = 0
    visited = [False for _ in range(n)]
    cnt = 0 # ile wierzchołków przerobiłem
    while cnt < n:
        val, u = Heap[0]
        # trzeba wierzchołek i oznaczyć jako odwiedzony
        delete(Heap, Gdzie_w_kopcu, n, Gdzie_w_kopcu[u])
        insert(inf, Heap, Gdzie_w_kopcu, n, u)
        visited[u] = True
        cnt += 1
        for el in G[u]:
            v, w = el
            if val + w < distance_a[v] and not visited[v] and val+w < Heap[Gdzie_w_kopcu[v]][0]:# musze dodać warunek spr wartość
                distance_a[v] = val + w
                delete(Heap, Gdzie_w_kopcu, n, Gdzie_w_kopcu[v])
                insert(val+w, Heap, Gdzie_w_kopcu, n, v)
                #dodaje wierzchołek

    return distance_a


"""
Opis:
Stosuje algorytm Dijkstry z wierzchołka s, by uzyskać drogę od s do każdego wierzchołka w grafie przed kradzieżą

Następnie przekształcam graf w taki sposób by koszt był równy 2*uprzedni koszt + łapówka.

Na tak przygotowanym grafie uruchamiam algorytm dijkstry z wierzchołka t, by uzyskać koszt ucieczki po kradzieży od każdego
wierzchołka do wierzchołka t.

Następnie sprawdzam w którym wierzchołku najbardziej opłaca się dokonać kradzieży.
Robię to poprzez poszukiwanie minimalnego kosztu podróży od s to wierzchołka x przed kradzieżą + kosztu podróży po kradzieży
od x do wierzchołka t - skradzione złoto z wierzchołka x. Czynność powtarzam dla każdego wierzchołka x należącego do G

Warto zauważyć że algorytm dijkstry, któy zaimplementowałem ma złożoność VlogV + E, gdyż kopiec który tworze ma rozmiar 
V i jeżeli wsadzam do niego najmniejszy koszt dotarcia do jakiegoś wierzchołka V`, to usuwam poprzedni. Wobec czego z
kopca będę wyjmował element maksymalnie V razy. Wkładanie i usuwanie z kopca ma złożoność logV.

Time: 
O(V) + O(VlogV + E) + O(V+E) + O(VlogV + E) + O(V) => O(VlogV + E)

"""

def gold(G,V,s,t,r):
  # tu prosze wpisac wlasna implementacje
  n = len(G) #O(V)
  #dijkstra od s bez kradnięcia
  Rabus_nie_kradnij = Dijkstra(s,G) #O(VlogV + E)
  #dijkstra od t kradnąc wszystko
  #przekształcam graf
  A = [[] for j in range(n)] #O(V)
  for i in range(n): #O (V+E)
    for j in range(len(G[i])):
      A[i].append([G[i][j][0], G[i][j][1]*2+r])
  Rabus_ukradl = Dijkstra(t,A) #O(VlogV + E)
  #Rozpatruje kradzież w każdym mieście
  result = Rabus_nie_kradnij[t]
  for i in range(n): #O(V)
    result = min(Rabus_ukradl[i] + Rabus_nie_kradnij[i] - V[i],result)

  return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
