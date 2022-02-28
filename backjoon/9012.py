from collections import deque

for _ in range(int(input())):
    q = deque()
    l = list(input())

    for i in l:
        if i == ')':
            if not q:
                q.append(i)
                break
            else:
                q.pop()
        else:
            q.append(i)

    if len(q) > 0:
        print("NO")
    else:
        print('YES')
