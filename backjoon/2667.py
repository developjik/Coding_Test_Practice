from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n = int(input())

g = [list(input()) for _ in range(n)]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    g[i][j] = '0'
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < len(g) and 0 <= ny < len(g) and g[nx][ny] == '1':
                g[nx][ny] = '0'
                q.append((nx, ny))
                count += 1

    return count


cnt = []
for i in range(n):
    for j in range(n):
        if g[i][j] == '1':
            cnt.append(bfs(i, j))

cnt.sort()
print(len(cnt))

for i in range(len(cnt)):
    print(cnt[i])
