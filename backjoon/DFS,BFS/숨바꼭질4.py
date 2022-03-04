from collections import deque
import copy

n, k = map(int, input().split())
g = [[-1, -1] for _ in range(10**5 + 1)]
g[n][0] = 0


def dfs(n):
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            return g[k]

        for i in [2*x, x-1, x+1]:
            if 0 <= i < 10**5+1 and g[i][0] == -1:
                g[i][0] = g[x][0] + 1
                g[i][1] = x
                q.append(i)


dfs(n)

print(g[k][0])

ans = [k]

while True:
    if g[k][1] != -1:
        ans.append(g[k][1])
        k = g[k][1]
    else:
        break


ans = ans[::-1]
print(*ans)
