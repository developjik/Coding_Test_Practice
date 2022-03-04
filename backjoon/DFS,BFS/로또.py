# s

import sys
sys.setrecursionlimit(10 ** 5)


def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(v[i], end=' ')
        print()
    else:
        for i in range(start, len(s)):
            v[depth] = s[i]
            dfs(i+1, depth+1)


while True:
    k, *s = map(int, input().split())

    if k == 0:
        break

    v = [0] * 6
    dfs(0, 0)
    print()
