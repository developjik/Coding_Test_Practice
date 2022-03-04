# n, s, m = map(int, input().split())
# lst = list(map(int, input().split()))
# dp1 = [0]*(m+1)
# dp2 = [0]*(m+1)

# dp1[s] = 1

# for v in lst:
#     for i in range(m+1):
#         if dp1[i]:
#             if i + v <= m:
#                 dp2[i+v] = 1
#             if i - v >= 0:
#                 dp2[i-v] = 1

#     if sum(dp2) == 0:
#         print(-1)
#         exit()
#     else:
#         dp1 = dp2
#         dp2 = [0]*(m+1)

# for i in range(m, -1, -1):
#     if dp1[i] == 1:
#         print(i)
#         break

from sys import stdin
input = stdin.readline

N,S,M = map(int, input().split())
V = list(map(int, input().split()))

res = [[0 for _ in range(M+1)] for _ in range(N+1)]
res[0][S] = 1

for i in range(1, N+1):
    for j in range(M+1):
        if res[i-1][j] == 0:
            continue
        if j + V[i-1] <= M:
            res[i][j+V[i-1]] = 1
        if j - V[i-1] >= 0:
            res[i][j-V[i-1]] = 1

idx = -1
for i in range(M, -1, -1):
    if res[N][i] == 1:
        idx = i
        break

print(idx)