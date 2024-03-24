# Algocja leży na wielkiej pustyni i składa się z miast oraz oaz połączonych drogami.
# Każde miasto jest otoczone murem i ma tylko dwie bramy—północną i południową. Z każdej bramy prowadzi
# dokładnie jedna droga do jednej oazy (ale do danej oazy może dochodzić dowolnie wiele dróg; oazy mogą też
# być połączone drogami między sobą). Prawo Algocji wymaga, że jeśli ktoś wjechał do miasta jedną bramą,
# to musi go opuścić drugą. Szach Algocji postanowił wysłać gońca, który w każdym mieście kraju odczyta
# zakaz formułowania zadań “o szachownicy” (obraza majestatu). Szach chce, żeby goniec odwiedził każde
# miasto dokładnie raz (ale nie ma ograniczeń na to ile razy odwiedzi każdą z oaz). Goniec wyjeżdża ze stolicji
# Algocji, miasta x, i po odwiedzeniu wszystkich miast ma do niej wrócić. Proszę przedstawić algorytm, który
# stwierdza czy odpowiednia trasa gońca istnieje

# sklejamy oazy

def super_glue(Graf, oazy):
    n = len(Graf)
    global list
    boll = [False for _ in range(n + 1)]
    list = [False for _ in range(n + 1)]
    for elem in oazy:
        boll[elem] = True
        list[elem] = True
    for elem in oazy:
        flag = False
        if boll[elem]:
            for i in range(len(Graf[elem])):
                a = Graf[elem]
                b = Graf[elem][i]
                if boll[Graf[elem][i]]:
                    flag = True
                    boll[Graf[elem][i]] = False

                    "0mergujemy listy"
                    Graf[elem] += Graf[Graf[elem][i]]
                    Graf[Graf[elem][i]] = [elem]
                    Graf[elem][i] = elem

            """wywalamy połaczenia pomiędzy połączonymi wierzchołkami"""
            if flag:
                k = 0
                while k < (len(Graf[elem])):
                    if Graf[elem][k] == elem:
                        del Graf[elem][k]
                        k-=1
                    k+=1
                """sortujemy i wywalamy powtórki"""
                Graf[elem] = sorted(set(Graf[elem]))

def dfs(graph, source, result,list):
    for i in range(len(graph[source])):
        a = graph[source][i]
        if list[graph[source][i]] and list[source]:
            dfs(graph, graph[source][i], result,list)
        else:

            b = None
            for j in range(len(graph[graph[source][i]])):
                if graph[graph[source][i]][j] == source:
                    b = j
                    break
            if b == None and list[source]:
                continue
            else:
                if b != None:
                    del graph[graph[source][i]][b]
                del graph[source][i]
                dfs(graph, a, result,list)
    result.append(source)


def eulerian_path(graph):
    result = []
    dfs(graph, 2, result,list)
    result.reverse()
    return result



oazy = [2, 4, 5, 7, 9]
Graf = [[2, 4], [2, 9], [0,1, 4, 3], [2, 5], [0, 2, 6], [3, 7, 8], [4, 7], [5, 6, 8], [5, 7], [1]]

def szachuj(Graf,oazy):
    super_glue(Graf,oazy)
    return eulerian_path(Graf)

print(szachuj(Graf,oazy))
