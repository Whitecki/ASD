from zad2testy import runtests
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

def Dijkstra(a,G,lenght):
    n = len(G)
    a*=4
    Heap = [(inf, i) for i in range(4*n)]
    Heap[a],Heap[0] = Heap[0], (0,a)
    Gdzie_w_kopcu = [i for i in range(4*n)]
    Gdzie_w_kopcu[a], Gdzie_w_kopcu[0] = Gdzie_w_kopcu[0], Gdzie_w_kopcu[a]
    distance_a = [inf for _ in range(4*n)]
    distance_a[a] = 0
    visited = [False for _ in range(4*n)]
    cnt = 0 # ile wierzchołków przerobiłem
    while cnt < 4*n:
        val, u= Heap[0]
        kierunek  = u % 4
        # trzeba wierzchołek i oznaczyć jako odwiedzony
        delete(Heap, Gdzie_w_kopcu, 4*n, Gdzie_w_kopcu[u])
        insert(inf, Heap, Gdzie_w_kopcu, 4*n, u)
        visited[u] = True
        cnt += 1
        # obracam się
        for i in range(1,4):
            if u // 4 == (u-i) //4:
                if i == 3 or i == 1:
                    bonus = 45
                else:
                    bonus  = 90
                if val + bonus < distance_a[u - i] and not visited[u-i] and val + bonus < Heap[Gdzie_w_kopcu[u-i]][0]:  # musze dodać warunek spr wartość
                    distance_a[u-i] = val + bonus
                    delete(Heap, Gdzie_w_kopcu, n, Gdzie_w_kopcu[u-i])
                    insert(val + bonus, Heap, Gdzie_w_kopcu, n, u-1)

        for i in range(1,4):
            if u // 4 == (u+i) //4:
                if i == 3 or i == 1:
                    bonus = 45
                else:
                    bonus  = 90
                if val + bonus < distance_a[u + i] and not visited[u+i] and val + bonus < Heap[Gdzie_w_kopcu[u+i]][0]:  # musze dodać warunek spr wartość
                    distance_a[u+i] = val + bonus
                    delete(Heap, Gdzie_w_kopcu, n, Gdzie_w_kopcu[u+i])
                    insert(val + bonus, Heap, Gdzie_w_kopcu, n, u+i)


        for vert,w in G[u//4]: # ide do innych wierzchołków
            flag = False
            if u //4 <= vert: #Gdzie jest wierzchołek, do którego idziemy
                if vert >= lenght + u //4: #poniżej
                    if u % 4 == 1:
                        flag = True
                else: # po prawo
                    if u % 4 == 0:
                        flag = True
            else:
                if u// 4 - lenght >= vert: # powyżej
                    if u % 4 == 3:
                        flag = True
                else: #po lewo
                    if u % 4 == 2:
                        flag = True
            v = vert*4 + u % 4
            if flag and  val + w < distance_a[v] and not visited[v] and val+w< Heap[Gdzie_w_kopcu[v]][0]:
                distance_a[v] = val + w
                delete(Heap, Gdzie_w_kopcu, n, Gdzie_w_kopcu[v])
                insert(val+w, Heap, Gdzie_w_kopcu, n, v)
                    #dodaje wierzchołek

    return distance_a


def robot( L, A, B ):
    height = len(L)
    lenght = len(L[0])
    # robię graf O(n**3)
    G = [[]for _ in range(height*lenght)]
    for i in range(height):
        for j in range(lenght):
            if L[i][j] != "X":
                #w góre
                y,x = i - 1,j
                while y > -1 and L[y][j] != "X":
                    if abs(y-i) > 2:
                        G[i*lenght + j].append([y*lenght+x,30*abs(y-i) + 40])
                    elif abs(y-i) == 2:
                        G[i * lenght + j].append([y * lenght + x, 100])
                    else:
                        G[i * lenght + j].append([y * lenght + x, 60])
                    y-=1
                #w dół
                y, x = i + 1, j
                while y < height and L[y][j] != "X":
                    if abs(y - i) > 2:
                        G[i * lenght + j].append([y * lenght + x, abs(y-i)*30 + 40])
                    elif abs(y - i) == 2:
                        G[i * lenght + j].append([y * lenght + x, 100])
                    else:
                        G[i * lenght + j].append([y * lenght + x, 60])
                    y += 1
                # w prawo
                y, x = i , j + 1
                while x < lenght and L[i][x] != "X":
                    if abs(x - j) > 2:
                        G[i * lenght + j].append([y * lenght + x, 30*abs(x-j) + 40])
                    elif abs(x - j) == 2:
                        G[i * lenght + j].append([y * lenght + x, 100])
                    else:
                        G[i * lenght + j].append([y * lenght + x, 60])
                    x += 1
                # w lewo
                y, x = i , j - 1
                while x > -1 and L[i][x] != "X":
                    if abs(x - j) > 2:
                        G[i * lenght + j].append([y * lenght + x, 30*abs(x-j) + 40])
                    elif abs(x - j) == 2:
                        G[i * lenght + j].append([y * lenght + x, 100])
                    else:
                        G[i * lenght + j].append([y * lenght + x, 60])
                    x -= 1
    #odpalam dijkstre z wierzchołka A
    distance = Dijkstra(A[0] + A[1]*lenght,G,lenght)
    if min(distance[(B[0]+ B[1]*lenght)*4],distance[(B[0]+ B[1]*lenght)*4+1],distance[(B[0]+ B[1]*lenght)*4+2],distance[(B[0]+ B[1]*lenght)*4] + 3) == inf:
        return None
    return min(distance[(B[0]+ B[1]*lenght)*4],distance[(B[0]+ B[1]*lenght)*4+1],distance[(B[0]+ B[1]*lenght)*4+2],distance[(B[0]+ B[1]*lenght)*4] + 3)


runtests( robot )


