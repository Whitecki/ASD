def insert(T, key):
    T.append(key)
    i = len(T) - 1
    while i > 0 and T[i] > T[(i - 1) // 2]:
        T[i], T[(i - 1) // 2] = T[(i - 1) // 2], T[i]
        i = (i - 1) // 2
    return T