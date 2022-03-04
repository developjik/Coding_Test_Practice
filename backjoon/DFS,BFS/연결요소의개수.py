from sys import stdin

input = stdin.readline

N, M = map(int, input().split())
G = [[0]*(N+1) for _ in range(N+1)]
V = [0]*(N+1)

for _ in range(M):
  x, y = map(int, input().split())
  G[x][y] = G[y][x] = 1

def dfs(v):
    V[v] = 1

    for i in range(1, N+1):
      if V[i] == 0 and G[i][v] == 1:
        dfs(i)

count = 0
for i in range(1, N+1):
  if V[i] == 0:
    dfs(i)
    count += 1

print(count)


