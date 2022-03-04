from sys import stdin

input = stdin.readline

n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
  for j in range(n):

    if i == n-1 and j == n-1:
      print(dp[i][j])
    
    tmp = g[i][j]

    if i + tmp < n:
      dp[i+tmp][j] += dp[i][j]
    
    if j + tmp < n:
      dp[i][j+tmp] += dp[i][j]
    