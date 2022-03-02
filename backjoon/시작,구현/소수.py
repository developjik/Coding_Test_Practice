m = int(input())
n = int(input())


def number(x):
    if x == 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True

ans = []
for i in range(m, n+1):
    if number(i):
        ans.append(i)

if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(ans[0])
