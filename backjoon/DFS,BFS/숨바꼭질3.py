from collections import deque

n, k = map(int, input().split())
g = [-1 for _ in range(10**5 + 1)]
g[n] = 0


def dfs(n):
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            print(g[k])
            break

        if 0 <= 2 * x < 10**5+1 and g[2 * x] == -1:
            g[2*x] = g[x]
            q.append(2 * x)

        for i in [x-1, x+1]:
            if 0 <= i < 10**5+1 and g[i] == -1:
                g[i] = g[x] + 1
                q.append(i)


dfs(n)
