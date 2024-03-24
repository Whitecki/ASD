
def dwaD(T:"wartość i-tego przedmiotu",W:"waga i-tego przedmiotu",H:"wysokość i-tego przedmiotu",maxW,maxH): #O(n*maxW*maxH)
    n = len(T)
    #dp[i][w][h] - max wartość rozpatrując i pierwszych przedmiotów, o maksymalnej wadze i wysokości kolejno w,h
    dp = [[[0 for _ in range(maxH+1)] for _ in range(maxW+1)] for _ in range(n)]
    if W[0] < maxW and H[0] < maxH:
        dp[0][W[0]][H[0]] = T[0]
    for i in range(n):
        for w in range(1,maxW+1):
            for h in range(1,maxH+1):
                dp[i][w][h] = dp[i-1][w][h]
                if w - W[i] >= 0 and h - H[i] >= 0:
                    dp[i][w][h] = max(dp[i][w][h],dp[i][w - W[i]][h - H[i]] + T[i])

    return dp[n-1][maxW][maxH]

T = [4, 10, 2, 3, 8]
W = [10, 4, 1, 2, 6]
H = [3, 9, 12, 4, 2]

MaxW = 12
MaxH = 20

print(dwaD(T,W,H,MaxW,MaxH))