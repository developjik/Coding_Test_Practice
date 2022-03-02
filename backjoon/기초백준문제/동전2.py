from sys import maxsize

n, k = map(int, input().split())
g = [int(input()) for _ in range(n)]
dp = [0] + [maxsize for _ in range(k)]

for i in g:
    for j in range(1, k+1):
        if j - i >= 0:
            dp[j] = min(dp[j-i] + 1, dp[j])

print(-1) if dp[-1] == maxsize else print(dp[-1])
