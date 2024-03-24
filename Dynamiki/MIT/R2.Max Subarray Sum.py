def krotki_kod(T):
    global_max, local_max = max(0,T[0]), max(0,T[0])
    for i in range(1,len(T)):
        if local_max + T[i] > T[i]:
            local_max += T[i]
        else:
            local_max = T[i]
        global_max = max(global_max,local_max)
    return global_max

T = [-9,1,-5,4,3,-6,7,8,-2]

print(krotki_kod(T))