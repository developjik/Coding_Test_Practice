from collections import deque
import sys

n = int(input())
g = [[-1] * 1001 for _ in range(1001)]
g[1][0] = 0

q = deque()
q.append((1, 0))

while q:

    s, c = q.popleft()

    if g[s][s] == -1:
        g[s][s] = g[s][c] + 1
        q.append((s, s))

    if s+c <= n and g[s+c][c] == -1:
        g[s+c][c] = g[s][c] + 1
        q.append((s+c, c))

    if s-1 >= 0 and g[s-1][c] == -1:
        g[s-1][c] = g[s][c]+1
        q.append((s-1, c))

ans = sys.maxsize
for i in range(n):
    if g[n][i] != -1:
        ans = min(ans, g[n][i])

print(ans)

