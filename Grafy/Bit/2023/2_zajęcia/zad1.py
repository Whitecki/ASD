"""
Nie ma sensu tracić czasu na implementacje tego zadania przed kolosem, więc tylko opisze algorytm
Tworzymy 100 wierzchołków, które łączymy krawędzi. Krawędzie są pomiędzy kolejnymi piętrami umieszczonymi w liście pięter
i o wadze równej prędkość*różnica pięter.
W taki sposób uzyskaliśmy multi graf. Skoro mamy uzyskać minimalny czas dotarcia z i do j. To możemy pozostawić pomiędzy
krawędziami tą o najmniejszej wadze.
Następnie odpalamy dijkstre z i :)))

"""