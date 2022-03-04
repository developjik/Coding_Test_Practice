from collections import deque

def bfs(target_x, target_y):
    while(q):
        x, y = q.popleft()

        if x == target_x and y == target_y:
            return g[target_x][target_y]

        for z in range(8):
            nx = x + dx[z]
            ny = y + dy[z]

            if 0 <= nx < l and 0 <= ny < l and g[nx][ny] == 0:
                q.append((nx, ny))
                g[nx][ny] = g[x][y] + 1


dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]

t = int(input())

for _ in range(t):

    l = int(input())

    g = [[0] * l for _ in range(l)]
    q = deque()

    x, y = map(int, input().split())
    g[x][y] = 1
    q.append((x, y))

    x, y = map(int, input().split())

    print(bfs(x, y)-1)
