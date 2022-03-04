import heapq
heap = []

arr = [list(map(int, input().split())) for _ in range(int(input()))]
arr.sort(key=lambda x: (x[0], x[1]))

for i in arr:
    if heap and heap[0] <= i[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, i[1])

print(len(heap))
