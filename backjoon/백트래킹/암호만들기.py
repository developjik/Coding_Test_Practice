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

input = stdin.readline
L, C = map(int, input().split())
alphabet = sorted(input().split())
visited = [0] * C

def check(string):
    count = 0
    for alpha in string:
        if alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u':
            count += 1
    return count


def dfs(depth, string, idx):
    if depth == L:
        if check(string) >= 1 and (len(string) - check(string)) >= 2:
            print(''.join(string))
            return

    for i in range(C):
        if idx < i:
            if not visited[i]:
                visited[i] = 1
                string.append(alphabet[i])
                dfs(depth + 1, string, i)
                visited[i] = 0
                string.pop()

dfs(0, [], -1)