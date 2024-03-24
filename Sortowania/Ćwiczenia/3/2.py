# QS bez rekurencji z wsłanym stosem
class Stack:
    def __init__(self):
        self.push = None
        self.pop = None
        self.isempty = False

def partition(A,p,r):
    pass

def QS_iterative(A,p,r):
    s = Stack()
    s.push((p,r))
    while s.isempty:
        (a,b) = s.pop
        if b > a:
            q = partition(A,p,r)
            if (b - q) > (q-a):
                s.push((q+1,b))
                s.push((a,q-1))
            else:
                s.push((a,q-1))
                s.push((q+1,b))

# 5 i 6 zadanie
# k chaotyczna tablica
