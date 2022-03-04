# from sys import stdin
# from itertools import combinations

# N, S = map(int, stdin.readline().split())
# nums = list(map(int, stdin.readline().split()))

# count = 0
# for i in range(len(nums)):
#     count += list(map(sum, combinations(nums, i+1))).count(S)

# print(count)

from sys import stdin
input = stdin.readline

N, S = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

global count
count = 0

def dfs(idx, sum):
    if idx >= N:
        return

    if sum + nums[idx] == S:
        global count
        count += 1

    dfs(idx+1, sum)
    dfs(idx+1, sum+nums[idx])

dfs(0, 0)

print(count)
