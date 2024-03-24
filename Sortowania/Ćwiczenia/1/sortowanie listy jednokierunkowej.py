def lenn(head):
    pass

def middle(head):
    pass

def MSll(head):
    n = lenn(head)
    if n > 1:
        mid = middle(head)
        Left = head
        Right = mid

        MSll(Left)
        MSll(Right)

        i,j,k = 0,0,0
        r,l = lenn(Right), lenn(Left)
        while r > i and l > j:
            if