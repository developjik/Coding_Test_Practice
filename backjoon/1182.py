# from sys import stdin
# from itertools import combinations

# N, S = map(int, stdin.readline().split())

# nums = list(map(int, stdin.readline().split()))

# count = 0
# for i in range(len(nums)):
#     count += list(map(sum, combinations(nums, i+1))).count(S)

# print(count)

from sys import stdin


def dfs(idx, sum, n, s, nums):
    if idx >= n:
        return

    if sum + nums[idx] == s:
        global count
        count += 1

    dfs(idx+1, sum, n, s, nums)
    dfs(idx+1, sum+nums[idx], n, s, nums)


N, S = map(int, stdin.readline().split())
nums = list(map(int, stdin.readline().split()))

global count
count = 0

dfs(0, 0, N, S, nums)

print(count)
