import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
ans = []

def backTracking(idx):
    for i in range(1, (idx//2) + 1):
        if ans[-i:] == ans[-2*i:-i]:
            return -1

    if idx == n:
        print(*ans, sep="")
        return 0

    for i in range(1, 4):
        ans.append(i)
        if backTracking(idx+1) == 0:
            return 0
        ans.pop()


backTracking(0)
