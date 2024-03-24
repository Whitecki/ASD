def minSwapsCouples(row):
    n = len(row)
    gdzie_lezy = [-1 for _ in range(2 * n)]
    for i in range(2 * n):
        gdzie_lezy[row[i]] = i
    cnt, i = 0, 0
    #szukamy niedobranej dwójki
    while row[i] + 1 == row[i + 1] or row[i + 1] + 1 == row[i]:
        i += 2
    start = row[i]
    return cnt
