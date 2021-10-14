from itertools import combinations

g = [int(input()) for _ in range(9)]
g.sort()

for i in combinations(g, 7):
    if sum(i) == 100:
        for j in i:
            print(j)
        exit()
