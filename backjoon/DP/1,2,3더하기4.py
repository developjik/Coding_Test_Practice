from sys import stdin
input = stdin.readline

t = int(input())
n_arr = []

for _ in range(t):
    n = int(input())
    n_arr.append(n)

dp = [1] * 10001

for i in range(2,10001):
    dp[i] += dp[i-2]

for i in range(3,10001):
    dp[i] += dp[i-3]

for i in n_arr:
    print(dp[i])
