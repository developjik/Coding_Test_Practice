from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

N = [int(input()) for i in range(N)]

count = 0
for i in range(len(N)-1, -1, -1):
    count += K // N[i]
    K = K % N[i]

print(count)