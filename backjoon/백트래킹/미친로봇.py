from sys import stdin
input = stdin.readline

dx , dy = [0, 0, -1, 1], [-1, 1, 0, 0]
N, *P = map(int, input().split())

g = [[0] * (2*N+1) for _ in range(2*N+1)]
g[N][N] = 1

def dfs(x, y, length, percent):
  global count

  if length == N:
    count += percent
    return

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<= nx < 2*N+1 and 0<= ny < 2*N+1 and g[nx][ny] == 0:
      g[nx][ny] = 1
      dfs(nx, ny, length+1, percent * 0.01 * P[i])
      g[nx][ny] = 0

count = 0
dfs(N,N,0, 1)
print(count)