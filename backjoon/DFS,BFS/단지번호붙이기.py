from collections import deque
from sys import stdin

input = stdin.readline

N = int(input())
G = [list(input()) for _ in range(N)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs (i, j):
  q = deque()
  q.append((i, j))
  G[i][j] = '0'

  count = 0

  while q:
    x, y = q.popleft()
    count += 1

    for k in range(4):
      nx = x + dx[k]
      ny = y + dy[k]

      if 0 <= nx < N and 0 <= ny < N and G[nx][ny] == '1':
        G[nx][ny] = '0'
        q.append((nx, ny))

  return count


ans = []
for i in range(N):
  for j in range(N):
    if G[i][j] == '1':
      ans.append(bfs(i, j))
ans.sort()

print(len(ans))

for i in ans:
  print(i)