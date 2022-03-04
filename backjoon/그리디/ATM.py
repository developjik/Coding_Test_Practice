from sys import stdin
input = stdin.readline

N = int(input())
G = list(map(int, input().split()))
G.sort()

ans = 0
wait = 0
for i in range(N):
  ans += G[i] + wait
  wait += G[i]

print(ans)

# N = int(input())

# arr = sorted(map(int, input().split()))

# time = 0
# for i in range(len(arr)):
#     time += sum(arr[:i+1])

# print(time)