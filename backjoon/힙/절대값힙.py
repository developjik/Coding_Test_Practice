import heapq
from sys import stdin

input = stdin.readline

heap = []

for i in range(int(input())):
    n = int(input())

    if n != 0:
      heapq.heappush(heap, [abs(n), n])
    else:
        if len(heap) == 0:
            print('0')
        else:
            print(heapq.heappop(heap)[1])