a, b = map(int, input().split())
g = []

for i in range(b):
    g.extend([(i+1)] * (i+1))

print(sum(g[a-1:b]))
