def dfs(x, y, level, p):
    global count

    if level == n:
        count += p
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < (2 * n) + 1 and 0 <= ny < (2 * n) + 1 and g[nx][ny] == 0:
            g[nx][ny] = 1
            dfs(nx, ny, level + 1, p * d[i] * 0.01)
            g[nx][ny] = 0


n, *d = map(int, input().split())
g = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]
g[n][n] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

count = 0
dfs(n, n, 0, 1)
print(count)
