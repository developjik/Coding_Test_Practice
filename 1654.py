from sys import stdin

input = stdin.readline

K, N = map(int, input().split())

lan = []

for _ in range(K):
    lan.append(int(input()))

start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2

    count = 0
    for i in lan:
        count += (i // mid)

    if count >= N:
        start = mid + 1
    else:
        end = mid-1

print(end)
