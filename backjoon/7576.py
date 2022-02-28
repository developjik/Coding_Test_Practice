from collections import deque

m, n = map(int, input().split())

g = []
q = deque()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    g.append(list(map(int, input().split())))

    for j in range(m):
        if g[i][j] == 1:
            q.append((i, j))


def bfs():
    while(q):
        x, y = q.popleft()

        for z in range(4):
            nx = x + dx[z]
            ny = y + dy[z]

            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
                q.append((nx, ny))
                g[nx][ny] = g[x][y] + 1


bfs()

ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(g[i]))

print(ans-1)
