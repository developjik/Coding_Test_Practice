from collections import deque

for _ in range(int(input())):
    n, m = map(int, input().split())
    q = deque(list(map(int, input().split())))

    if n == 1:
        print(1)
    else:
        cnt = 0

        while q:
            m = (m+len(q)-q.index(max(q))) % len(q) - 1
            q.rotate(len(q)-q.index(max(q)))
            q.popleft()
            cnt += 1

            if m == -1:
                print(cnt)
                break
