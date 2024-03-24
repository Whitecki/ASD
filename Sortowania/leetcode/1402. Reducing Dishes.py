# A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.
# Like-time coefficient of a dish is defined as the time taken to cook that dish including previous dishes multiplied by
# its satisfaction level i.e. time[i] * satisfaction[i].
# Return the maximum sum of like-time coefficient that the chef can obtain after dishes preparation.
# Dishes can be prepared in any order and the chef can discard some dishes to get this maximum value.


def maxSatisfaction(satisfaction):
    satisfaction.sort()
    n = len(satisfaction)
    i = 0
    while i < n and satisfaction[i] < 0:
        i += 1
    base = 0
    for j in range(i,n):
        base += satisfaction[j]
    if i != 0:
        i-= 1
        while i > -1 and satisfaction[i] + base >= 0:
            base += satisfaction[i]
            i-= 1
        i += 1
    result = 0
    for a in range(1,n-i+1):
        result += a*satisfaction[i]
        i+= 1
    return result

T = [-1,-8,0,5,-9]
print(maxSatisfaction(T))