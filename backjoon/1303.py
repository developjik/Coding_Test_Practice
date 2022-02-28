from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
g = [list(input()) for _ in range(m)]
v = [[0] * n for _ in range(m)]

res_w = 0
res_b = 0


def bfs(i, j, cnt, key):
    q = deque()
    g[i][j] = 0
    q.append((i, j))
    cnt += 1

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < m and 0 <= ny < n and g[nx][ny] == key:
                g[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1

    return cnt


for i in range(m):
    for j in range(n):
        if g[i][j] == 'W':
            res_w += bfs(i, j, 0, 'W') ** 2

        if g[i][j] == 'B':
            res_b += bfs(i, j, 0, 'B') ** 2

print(res_w, res_b)
