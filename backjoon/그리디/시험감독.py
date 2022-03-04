from sys import stdin
input = stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0
for i in A:
  if i > 0:
    ans += 1
    tmp = i-B

    if tmp > 0:
      ans += tmp // C
      
      if tmp % C != 0:
        ans += 1

print(ans)