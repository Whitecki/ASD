# Dana jest klasa :
# class Node:
#       val = 0
#       next = None
# reprezentująca węzeł jednokierunkowego łańcucha odsyłaczowego, w którym wartości val poszczególnych węzłów zostały
# wygenerowane zgodnie z rozkładem jednostajnym na przedziale [a, b]. Napisz procedurę sort(first), która sortuje taką
# listę. Funkcja powinna być jak najszybsza. ​

'''idea: zliczam długość tego łańcucha(O(n)). Robię guardiany, symbolizujące bucket-y, w ilości n. Następnie przepinam
do odpowiednich guardianów. Sortuje je. Następnie scalam te listy w jedną
'''