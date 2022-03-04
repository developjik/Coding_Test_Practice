N = int(input())
dp = [0] * (N+1)
T = []
P = []

for _ in range(N):
    a, b = map(int, input().split())
    T.append(a)
    P.append(b)

for i in range(N):
    if T[i] + i <= N:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i] + P[i])
    dp[i+1] = max(dp[i+1], dp[i])
print(dp[N])
