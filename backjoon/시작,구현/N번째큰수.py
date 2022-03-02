for _ in range(int(input())):
    g = list(map(int, input().split()))
    g.sort()

    print(g[-3])
