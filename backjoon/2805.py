from sys import stdin

N, M = map(int, stdin.readline().split())

namu = list(map(int, stdin.readline().split()))

start = 0
end = max(namu)

while start <= end:
    mid = (start + end) // 2

    tmp = 0
    for i in namu:
        if i > mid:
            tmp += (i-mid)

    if tmp >= M:
        start = mid + 1
    else:
        end = mid-1


print(end)
