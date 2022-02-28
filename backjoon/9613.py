from math import gcd
from itertools import combinations

for _ in range(int(input())):
    N, *arr = map(int, input().split())

    ans = 0
    for i in list(combinations(arr, 2)):
        ans += gcd(i[0], i[1])

    print(ans)
