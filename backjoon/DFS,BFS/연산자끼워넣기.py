
def dfs(cnt, result, plus, minnus, mul, div):
    global global_max
    global global_min

    if cnt == n:
        global_max = max(global_max, result)
        global_min = min(global_min, result)

    if plus:
        dfs(cnt+1, result + g[cnt], plus-1, minnus, mul, div)
    if minnus:
        dfs(cnt+1, result - g[cnt], plus, minnus-1, mul, div)
    if mul:
        dfs(cnt+1, result * g[cnt], plus, minnus, mul-1, div)
    if div:
        dfs(cnt+1, -(-result // g[cnt]) if result <
            0 else result // g[cnt], plus, minnus, mul, div-1)


n = int(input())
g = list(map(int, input().split()))
s = list(map(int, input().split()))

global_max = -10 ** 9
global_min = 10 ** 9

dfs(1, g[0], s[0], s[1], s[2], s[3])

print(global_max)
print(global_min)
