from collections import deque

n, m = map(int, input().split())

deq = deque([i+1 for i in range(n)])
ans = []

while len(deq) != 0:
    deq.rotate(len(deq) - m)
    print(deq)
    ans.append(str(deq.pop()))

print("<", ", ".join(ans), ">", sep='')
