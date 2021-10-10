from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m, k = map(int, input().split())

g = [[0]*(m+1) for _ in range(n+1)]

for _ in range(k):
    x, y = map(int, input().split())
    g[x][y] = 1


def dfs(x, y):
    count = 0
    q = deque()
    q.append((x, y))
    g[x][y] = 0

    while q:
        i, j = q.popleft()
        count += 1

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if 1 <= nx < n+1 and 1 <= ny < m+1 and g[nx][ny] == 1:
                q.append((nx, ny))
                g[nx][ny] = 0

    return count


ans = 0

for x in range(1, n+1):
    for y in range(1, m+1):
        if g[x][y] == 1:
            ans = max(ans, dfs(x, y))

print(ans)
