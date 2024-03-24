# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

"""
idea: Korzystamy ze struktury Find-Union. Tworzymy 26 Node-ów symbolizujących litery i nadajemy im rank wg zasady: im
wcześniej w alfabecie tym większy. Następnie tworzymy drzewa. Root jest literą na jaką trzeba zamienić wszystkie "niżej"
występujące litery.
time complexity: O( N + M + log∣Σ∣ )
"""

class Node:
    def __init__(self, value, rank):
        self.value = value
        self.parent = self
        self.rank = rank

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)

    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False

    if x.rank > y.rank:
        y.parent = x

    else:
        x.parent = y
    return True

def smallestEquivalentString(s1, s2, baseStr):
    Alphabet = [Node(chr(i+97),26 - i) for i in range(26)]
    n = len(s1)
    m = len(baseStr)
    for i in range(n):
        if s1[i] != s2[i]:
            union(Alphabet[ord(s1[i])-97],Alphabet[ord(s2[i])-97])

    #prep
    Betha = [-1 for _ in range(26)]
    for i in range(26):
        x = Alphabet[i]
        while x.parent != x:
            x = x.parent
        Betha[i] = x.value

    result = ""
    for j in range(m):
        result += Betha[ord(baseStr[j]) - 97]

    return result

"""
s1 = "parker"
s2 = "morris"
baseStr = "parser"

s1 = "hello"
s2 = "world"
baseStr = "hold"
"""

s1 = "leetcode"
s2 = "programs"
baseStr = "sourcecode"

print(smallestEquivalentString(s1,s2,baseStr))