from collections import deque

n, k = map(int, input().split())
g = [[-1, 0] for _ in range(10**5 + 1)]
g[n][0] = 0
g[n][1] = 1


def dfs(n):
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        for i in [x-1, x+1, 2*x]:
            if 0 <= i < 10**5+1:
                if g[i][0] == -1:
                    g[i][0] = g[x][0] + 1
                    g[i][1] = g[x][1]
                    q.append(i)

                elif g[i][0] == g[x][0] + 1:
                    g[i][1] += g[x][1]


dfs(n)

for i in g[k]:
    print(i)
