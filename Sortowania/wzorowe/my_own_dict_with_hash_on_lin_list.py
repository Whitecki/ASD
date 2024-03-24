class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def __setitem__(self, key, value):
        index = self.hash_function(key)
        node = self.table[index]
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def __getitem__(self, key):
        index = self.hash_function(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next

    def __delitem__(self, key):
        index = self.hash_function(key)
        node = self.table[index]
        if node and node.key == key:
            self.table[index] = node.next
            return
        while node and node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next
        raise KeyError(key)

    def __contains__(self, key):
        index = self.hash_function(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return True
            node = node.next
        return False

    def keys(self):
        for node in self.table:
            while node:
                yield node.key
                node = node.next

    def values(self):
        for node in self.table:
            while node:
                yield node.value
                node = node.next

    def items(self):
        for node in self.table:
            while node:
                yield (node.key, node.value)
                node = node.next

from random import randint
# my_dict = HashTable(10)
# for i in range(100):
#     my_dict[randint(1,20)] = randint(1,1000)
#     my_dict[randint(1,20)] = randint(1,1000)
#
# print(my_dict[18])
for i in range(100):
    tab = [False for _ in range(101)]
    tab[(hash(i) % 100)] = True
    print((hash(i) % 100))
for el in tab:
    if el:
        print("1")



