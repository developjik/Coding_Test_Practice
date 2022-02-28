import sys
from collections import deque

input = sys.stdin.readline

deq = deque()

for i in range(int(input())):
    mission = list(input().split())

    if mission[0] == 'push_front':
        deq.appendleft(mission[1])
    elif mission[0] == 'push_back':
        deq.append(mission[1])
    elif mission[0] == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif mission[0] == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif mission[0] == 'size':
        print(len(deq))
    elif mission[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif mission[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif mission[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])

