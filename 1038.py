from sys import stdin
from itertools import combinations

n = int(stdin.readline())

nums = []
for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        nums.append(int("".join(map(str, comb))))

nums.sort()

try:
    print(nums[n])
except:
    print(-1)
