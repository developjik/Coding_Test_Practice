import sys
from collections import deque

dx = [1, 1, 1, 0, -1, -1, -1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]
n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if g[i][j] == 1:
            q.append((i, j))

while q:
    x, y = q.popleft()

    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
            g[nx][ny] = g[x][y] + 1
            q.append((nx, ny))

ans = 0
for i in range(n):
    ans = max(max(g[i]), ans)

print(ans-1)
