from collections import deque

n = int(input())
g = [[0] * (n+1) for _ in range(n+1)]
v = [0] * (n+1)

for _ in range(int(input())):
    i, j = map(int, input().split())
    g[i][j] = g[j][i] = 1


def bfs(x):
    q = deque()
    q.append(x)
    v[x] = 1
    cnt = 0

    while q:
        i = q.popleft()
        cnt += 1

        for j in range(1, n+1):
            if g[i][j] == 1 and v[j] == 0:
                q.append(j)
                v[j] = 1

    return cnt-1


print(bfs(1))
