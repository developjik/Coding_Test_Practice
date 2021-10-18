n, k = map(int, input().split())

g = [i+1 for i in range(n) if n % (i+1) == 0]

if len(g) < k:
    print(0)
else:
    print(g[k-1])
