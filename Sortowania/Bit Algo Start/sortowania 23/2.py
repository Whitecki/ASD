# Dana jest tablica 2n liczb rzeczywistych. Zaproponuj algorytm, który podzieli te liczby na n par w taki sposób, że
# podział będzie miał najmniejszą maksymaln= sumę liczb w parze. Przykładowo, dla liczb (1,3,5,9) możemy mieć podziały
# ((1,3),(5,9)), ((1,5),(3,9)), oraz ((1,9),(3,5)). Sumy par dla tych podziałów to (4,14), (6,12) oraz (10,8), w związku
# z tym maksymalne sumy to 14, 12 oraz 10. Wynika z tego, że ostatni podział ma najmniejszą maksymalną sumę

#sortuje tablice T. Następnie łącze najwiekszy z najmniejszym elementem, aż skończy się lista

# czy ten problem ma optymalną podstrukturę(jak ją wykazać?) i greedy choices

def f(T):
    T.sort()
    n = len(T)
    result = []
    for i in range(n//2):
        result.append((T[i],T[n-1-i]))

    return result