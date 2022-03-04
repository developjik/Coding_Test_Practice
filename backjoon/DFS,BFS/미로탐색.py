from collections import deque

dx , dy = [0, 0, -1, 1], [1, -1, 0, 0]

n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]

v = [[0]*m for _ in range(n)]
v[0][0] = 1

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()

    if x == n-1 and y == m-1:
        print(v[x][y])
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < n and 0<= ny < m:
            if v[nx][ny] == 0 and matrix[nx][ny] == '1':
                v[nx][ny]= v[x][y] +1
                q.append((nx,ny))