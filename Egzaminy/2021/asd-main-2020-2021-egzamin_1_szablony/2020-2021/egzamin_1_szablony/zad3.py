from zad3testy import runtests

def kintersect( A, k ):
  """Miejsce na Twoją implementację"""
  #dp[i][j][k] - krawędzie przecięcia najdłuższego przedziału z k przedziałów do odcinku i
  n = len(A)
  sorted(A,key=lambda x: x[1])
  dp = [[[(A[i][0], A[i][1]) if kk == 1 and i == j else (0,0) for kk in range(k+1)] for j in range(n)] for i in range(n)]
  parent = [[[None if kk == 1 and i == j else (0,0) for kk in range(k+1)] for j in range(n)] for i in range(n)]
  for kk in range(2,k+1): #ilość kk przedziałów należących do najdłuższego przecięcia odcinków to i-tego
    for koniec in range(1,n): # długość odcinka
      dl = 0
      zakres = (0, 0)
      for j in range(i):
        if dp[l][i][k-1][1] - dp[l][i][k-1][0] > dl:
          dl = dp[l][i][k-1][1] - dp[l][i][k-1][0]
          zakres = (dp[l][i][k-1][0], dp[l][i][k-1][1])
          # parent[i][j][k] = (l,i,k-1)
      dp[i][j][k] = zakres
  maxi = 0
  idx = -1
  for i in range(n):
    for j in range(n):
      if maxi < dp[i][j][k][1] - dp[i][j][k][0]:
        maxi = dp[i][j][k][1] - dp[i][j][k][0]
  return list(range(k))

runtests( kintersect )