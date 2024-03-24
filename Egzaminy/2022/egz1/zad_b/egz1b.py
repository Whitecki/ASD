from egz1btesty import runtests


class Node:
    def __init__(self):
        self.left = None  # lewe poddrzewo
        self.right = None  # prawe poddrzewo
        self.x = None  # pole do wykorzystania przez studentow


def wideentall(T):
    start = T
    arr = [0]
    arr_len = 0
    cnt = 0

    def schodze_w_dol(s, h):
        s.x = h
        nonlocal cnt, arr_len
        cnt += 1
        if arr_len < h:
            arr.append(0)
            arr_len += 1
        arr[h] += 1
        if s.left is not None:
            schodze_w_dol(s.left, h + 1)
            s.x = s.left.x
        if s.right is not None:
            schodze_w_dol(s.right, h + 1)
            s.x = max(s.x, s.right.x)

    schodze_w_dol(start, 0)
    idx_max, val_max = 0, 0
    for i in range(arr_len + 1):
        if arr[i] >= val_max:
            val_max, idx_max = arr[i], i
    odciete = 0

    def podcinamy(s, h, cel):
        nonlocal odciete
        if s.left is not None:
            if s.left.x < cel:
                odciete += 1
            elif cel == h:
                odciete += 1
            else:
                podcinamy(s.left, h + 1, cel)
        if s.right is not None:
            if s.right.x < cel:
                odciete += 1
            elif cel == h:
                odciete += 1
            else:
                podcinamy(s.right, h + 1, cel)

    start2 = T
    podcinamy(start2, 0, idx_max)
    return odciete


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(wideentall, all_tests=True)
