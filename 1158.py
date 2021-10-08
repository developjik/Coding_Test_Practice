import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

deq = deque([i+1 for i in range(n)])
ans = []

while len(deq) != 0:
    deq.rotate(len(deq) - m)
    ans.append(str(deq.pop()))

print("<", ", ".join(ans), ">", sep='')
