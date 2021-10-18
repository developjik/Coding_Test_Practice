g = []

for _ in range(7):
    n = int(input())

    if n % 2 != 0:
        g.append(n)

if len(g) == 0:
    print(-1)
else:
    print(sum(g))
    print(min(g))
