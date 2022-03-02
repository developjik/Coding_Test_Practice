n = int(input())
g = list(map(int, input().split()))
m = max(g)

g = [i/m*100 for i in g]
print(sum(g)/len(g))
