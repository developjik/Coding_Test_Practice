from collections import deque

a, b = map(int, input().split())

q = deque([(a, 1)])

while q:
    value, count = q.popleft()

    if value == b:
        print(count)
        exit(0)

    for i in [value * 2, int(str(value)+'1')]:
        if 1 <= i <= b:
            q.append((i, count + 1))

print(-1)
