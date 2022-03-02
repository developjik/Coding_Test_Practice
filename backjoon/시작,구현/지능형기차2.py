g = [list(map(int, input().split())) for _ in range(10)]

count = 0
ans = 0

for i in range(10):
    count -= g[i][0]

    if ans < count:
        ans = count

    count += g[i][1]

    if ans < count:
        ans = count

print(ans)
