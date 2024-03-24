"""
Pierwszy pomysł:
sortuje tablice meetings po czasach
następnie z krawędzi o tym samym czasie, robie graf O(V+E)
odpalam dfs z wszystkich już wiedzących sekret ludzi
dodaje nowych ludzi do listy wiedzących
powtarzam cały proces, aż przejdę po wszystkich
nwm w sumie czy stworzyć jedną listę sąsiedztwa, czy tworzyć dla każdego nowego grafu

Lepszy pomysł:
tworze graf
Z początkowego wierzchołka chodzę po rosnących wagach. Ważne jest zauważenie, że moge wejść do jakiegoś wierzchołka
kolejny raz. Normalnie oznaczałoby to niebezpieczny precedens, zwiastujący rozwiązanie nie wielomianowe. Warto jednak
zauważyć, że wejście do jakiegoś wierzchołka w którym już byliśmy oznacza, że możemy ponownie przejść po jego krawędziach.
Jeżeli wartość z jaką wchodzimy jest mniejsza, to istnieje szansa, że stworzymy nową nieodwiedzoną ścieżkę. Po już
 odwiedzonych nie ma sensu chodzić, bo nic to nie da.
"""

def findAllPeople(n, meetings, firstPerson):
    pass