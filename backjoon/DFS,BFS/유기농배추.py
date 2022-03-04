from sys import stdin
from collections import deque

input = stdin.readline
T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(matrix, i, j):
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                q.append((nx, ny))


for _ in range(T):
    count = 0
    N, M, K = map(int, stdin.readline().split())
    matrix = [[0] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        matrix[y][x] = 1

    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1:
                bfs(matrix, i, j)
                count += 1

    print(count)
