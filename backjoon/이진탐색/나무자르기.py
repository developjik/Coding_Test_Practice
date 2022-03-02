from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

namu = list(map(int, input().split()))

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
