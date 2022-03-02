import heapq

for _ in range(int(input())):
    m = int(input())
    g = []

    while len(g) != m:
        g.extend(list(map(int, input().split())))

    print((len(g)+1) // 2)

    max_heap = []
    min_heap = []
    cnt = 0

    for i in range(len(g)):

        if i % 2 == 0:
            heapq.heappush(max_heap, -g[i])
        else:
            heapq.heappush(min_heap, g[i])

        if len(max_heap) > 0 and len(min_heap) > 0 and min_heap[0] < -max_heap[0]:
            ma = - heapq.heappop(max_heap)
            mi = - heapq.heappop(min_heap)

            heapq.heappush(max_heap, mi)
            heapq.heappush(min_heap, ma)

        if i % 2 == 0:
            if cnt != 0 and cnt % 10 == 0:
                print()

            print(-max_heap[0], end=' ')
            cnt += 1

    print()
