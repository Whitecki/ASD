from math import inf

def MissingNumber(array,n):
    maxx = False
    pot = 0
    array = [0] + array[:]
    n+=1
    for i in range(1,n):
        while array[i] != i and array[i] != []:
            if array[i] < n:
                tmp = array[array[i]]
                array[array[i]] = array[i]
                array[i] = tmp
            else:
                maxx = True
                array[i] = []
        if array[i] == []:
            pot = i

    if maxx:
        return pot
    return n


array = [1,2,3,5]
n = len(array)
print(MissingNumber(array,n))
