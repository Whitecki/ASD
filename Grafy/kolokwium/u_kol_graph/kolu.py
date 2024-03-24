from kolutesty import runtests
from queue import Queue

def swaps( disk, depends ):
    # zakładam że zadanie da się rozwiązać <=> graf jest Dagiem
    n = len(depends)
    #zliczam ile chodzi kresek do każdej kropki
    dp = [0 for _ in range(n)]
    for a in depends:
        for b in a:
            dp[b] += 1
    dpp = [dp[i] for i in range(n)]
    A = Queue()
    AA = Queue()
    B = Queue()
    BB = Queue()
    a,b = 0,0
    #jeżeli nie wchodzi żadna kreska do kropki, to wsadzam ją do odpowiadającej kolejki
    for i in range(n):
        if not dp[i]:
            if disk[i] == "A":
                A.put(i)
                AA.put(i)
            else:
                B.put(i)
                BB.put(i)


    result = ["A"]
    while not A.empty() or not B.empty():
        while (result[-1] == "B" or A.empty()) and not B.empty():
            u = B.get()
            result.append("B")
            for v in depends[u]:
                dp[v] -= 1
                if dp[v] == 0:
                    if disk[v] == "A":
                        A.put(v)
                    else:
                        B.put(v)
        while (result[-1] == "A" or B.empty()) and not A.empty():
            u = A.get()
            result.append("A")
            for v in depends[u]:
                dp[v] -= 1
                if dp[v] == 0:
                    if disk[v] == "A":
                        A.put(v)
                    else:
                        B.put(v)
    cnt = 0
    for i in range(2,len(result)):
        if result[i] != result[i-1]:
            cnt += 1

    result = ["B"]
    while not AA.empty() or not BB.empty():
        while (result[-1] == "B" or AA.empty()) and not BB.empty():
            u = BB.get()
            result.append("B")
            for v in depends[u]:
                dpp[v] -= 1
                if dpp[v] == 0:
                    if disk[v] == "A":
                        AA.put(v)
                    else:
                        BB.put(v)
        while (result[-1] == "A" or BB.empty()) and not AA.empty():
            u = AA.get()
            result.append("A")
            for v in depends[u]:
                dpp[v] -= 1
                if dpp[v] == 0:
                    if disk[v] == "A":
                        AA.put(v)
                    else:
                        BB.put(v)


    cntt = 0
    for i in range(2,len(result)):
        if result[i] != result[i-1]:
            cntt += 1
    return min(cnt,cntt)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( swaps, all_tests = True )

