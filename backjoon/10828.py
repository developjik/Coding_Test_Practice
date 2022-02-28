import sys
from collections import deque

input = sys.stdin.readline

deq = deque()

for i in range(int(input())):
    mission = input().split()

    if mission[0] == 'push':
        deq.append(mission[1])
    elif mission[0] == 'pop':
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
    elif mission[0] == 'top':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
