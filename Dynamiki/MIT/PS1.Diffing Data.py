# Operating system Menix has a diff utility that can compare files. A file is an ordered sequence of strings,
# where the ith string is called the ith line of the file. A single change to a file is either:
# • the insertion of a single new line into the file;
# • the removal of a single line from the file; or
# • swapping two adjacent lines in the file.
# In Menix, swapping two lines is cheap, as they are already in the file, but inserting or deleting a line is
# expensive. A diff from a file A to a file B is any sequence of changes that, when applied in sequence to A
# will transform it into B, under the conditions that any line may be swapped at most once and any pair of
# swapped lines appear adjacent in A and adjacent in B. Given two files A and B, each containing exactly
# n lines, describe an O(kn + n**2)-time algorithm to return a diff from A to B that minimizes the number of
# changes that are not swaps, assuming that any line from either file is at most k ASCII characters long

# wykonam zadanie zamiany napisu A w napis B, preprocessing pozostawiam dla potomnych
# cel zadania: znaleźc minimalną ilość operacji by napis A zamienić w B

from math import inf

def strings(A,B):
    a,b = len(A),len(B)
    # Na początku musimy znaleźć optymalną podstrukturę. Spróbuję na początek wziąć suffixy obu wyrazów.
    # subproblems: najmniejsza ilość zmian w wyrazach A[:i] i B[:j]
    dp = [[inf for _ in range(a+1)] for _ in range(b+1)]

    #Base case: 1) pusty wyraz A i pusty wyraz, nie wymagają zmian, natomiast jesli tylko jeden z wyrazów jest pusty, to
    # ilość zmian jest równa długości tego niepustego
    dp[0][0] = 0
    for i in range(a+1):
        dp[0][i] = i
    for i in range(b+1):
        dp[i][0] = i

    # topological order: z rekurencyjnego zapisu funkcji, wynika że aby rozwiązać podproblem dp[j][i], potrzebuje
    # podproblemów o mniejszych/równych wartościach j,i
    for j in range(1,b+1):
        for i in range(1,a+1):

            if A[i-1] == B[j-1]: # jeżeli literka jest taka sama, to biorę wartość bez tych dwóch literek
                dp[j][i] = dp[j-1][i-1]
            elif A[i-2] == B[j-1] and A[i-1] == B[j-2] and i > 1 and j > 1: # swap
                dp[j][i] = dp[j-2][i-2]
            else:
                dp[j][i] = min(dp[j-1][i],dp[j][i-1]) + 1 # usuwam lub dodaje

    return dp[b][a]

A = "Alai"
B = "Alib"
print(strings(A,B))
