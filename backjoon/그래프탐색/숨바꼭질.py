from collections import deque

n, k = map(int, input().split())
max = 100000
v = [0] * (max+1)

q = deque()
q.append(n)

while q:
    x = q.popleft()

    if x == k:
        print(v[k])
        break

    for i in (x - 1, x+1, 2*x):
        if 0 <= i <= max and v[i] == 0:
            v[i] = v[x] + 1
            q.append(i)
