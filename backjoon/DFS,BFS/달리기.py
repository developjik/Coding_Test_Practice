from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m, k = map(int, input().split())
g = [list(input()) for _ in range(n)]
v = [[float('inf')]*m for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())


def dfs(x, y):
    q = deque()
    q.append((x, y))
    v[x][y] = 0

    while q:
        i, j = q.popleft()

        if i == x2 - 1 and j == y2 - 1:
            return v[i][j]

        for a in range(4):
            nx = i + dx[a]
            ny = j + dy[a]

            tmp = 1
            while tmp <= k and 0 <= nx < n and 0 <= ny < m and g[nx][ny] != '#' and v[nx][ny] > v[i][j]:

                if v[nx][ny] == float('inf'):
                    v[nx][ny] = v[i][j] + 1
                    q.append((nx, ny))

                nx += dx[a]
                ny += dy[a]

                tmp += 1
    return -1


print(dfs(x1-1, y1-1))
