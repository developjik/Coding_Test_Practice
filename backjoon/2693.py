t = int(input())

for _ in range(t):
    g = list(map(int, input().split()))
    g.sort()

    print(g[-3])
