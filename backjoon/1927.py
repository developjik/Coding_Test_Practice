import heapq
from sys import stdin, stdout

input = stdin.readline

heap = []

for _ in range(int(input())):
    n = int(input())

    if n > 0:
        heapq.heappush(heap, n)
    else:
        if len(heap) == 0:
            print('0')
        else:
            print(heapq.heappop(heap))
