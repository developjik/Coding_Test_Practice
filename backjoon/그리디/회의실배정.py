from sys import stdin
input = stdin.readline

arr = [list(map(int, input().split())) for _ in range(int(input()))]
arr.sort(key=lambda x: (x[1], x[0]))

count = 0
last = 0
for start, end in arr:
    if start >= last:
        count += 1
        last = end

print(count)
