# Dana jest tablica A mająca n liczb naturalnych przyjmujących wartości z zakresu [0...n]. Proszę napisać algorytm
# znajdujący rozmiar największego podzbioru liczb z A, takiego, że ich GCD jest różny od 1. Algorytm powinien działać
# jak najszybciej.

'''jest n//6 + c dzielników. Jednak jeżeli weźmiemy pod uwagę, że liczby pierwsze, większe od pierwiastka z n dzielą się
 tylko przez sb i 1, to mogą one tworzyć podzbiór tylko z powtórkami tej samej liczby, lub jej wielokrotnościami.
  dla każdego robimy licznik, który później'''

def counting_sort(T,n):
    A = [0 for _ in range(n+1)]
    for el in T:
        A[el] += 1
    a = 0
    maxi = 0
    for i in range(n+1):
        maxi = max(maxi,A[i])
        for j in range(A[i]):
            T[a] = i
            a += 1
    return maxi
def f(T):
    n = len(T)
    counting_sort(T,n)
    divides = [2,3]
    i = 5
    while i < n**(0.5) +1:
        divides.append(i)
        divides.append(i+2)
        i+= 6
    for i in range(n):
        for el in divides:
            if T[i] != 1:
                pass

'''bonus w postaci słownika, którego nie mam serca usuwać'''
# class Node:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None
#
#
# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [None] * size
#
#     def hash_function(self, key):
#         return hash(key) % self.size
#
#     def __setitem__(self, key, value):
#         index = self.hash_function(key)
#         node = self.table[index]
#         while node:
#             if node.key == key:
#                 node.value = value
#                 return
#             node = node.next
#         new_node = Node(key, value)
#         new_node.next = self.table[index]
#         self.table[index] = new_node
#
#     def __getitem__(self, key):
#         index = self.hash_function(key)
#         node = self.table[index]
#         while node:
#             if node.key == key:
#                 return node.value
#             node = node.next
#
#     def __delitem__(self, key):
#         index = self.hash_function(key)
#         node = self.table[index]
#         if node and node.key == key:
#             self.table[index] = node.next
#             return
#         while node and node.next:
#             if node.next.key == key:
#                 node.next = node.next.next
#                 return
#             node = node.next
#
#     def __contains__(self, key):
#         index = self.hash_function(key)
#         node = self.table[index]
#         while node:
#             if node.key == key:
#                 return True
#             node = node.next
#         return False
#
#     def keys(self):
#         for node in self.table:
#             while node:
#                 yield node.key
#                 node = node.next
#
#     def values(self):
#         for node in self.table:
#             while node:
#                 yield node.value
#                 node = node.next
#
#     def items(self):
#         for node in self.table:
#             while node:
#                 yield (node.key, node.value)
#                 node = node.next
#

