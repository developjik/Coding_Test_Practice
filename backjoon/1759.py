# from sys import stdin
# from itertools import combinations

# L, C = map(int, stdin.readline().split())

# C = sorted((stdin.readline().split()))

# for i in combinations(C, L):
#     vowel = 0
#     no_vowel = 0

#     for j in i:
#         if j in ['a', 'e', 'i', 'o', 'u']:
#             vowel += 1
#         else:
#             no_vowel += 1

#     if vowel >= 1 and no_vowel >= 2:
#         print("".join(i))


from sys import stdin


def dfs(idx, ans, count, L, C):
    if idx == len(C):
        return "".join(ans)

    # if len(ans) + len(C)-idx < L:
    #     return

    dfs(idx+1, ans, count, L, C)
    ans.append(C[idx])
    dfs(idx+1, ans, count+1, L, C)


L, C = map(int, stdin.readline().split())
C = sorted((stdin.readline().split()))

dfs(0, [], 0, L, C)
