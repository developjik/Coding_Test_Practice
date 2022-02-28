n = int(input())

g = map(int, input().split())


def number(x):
    if x == 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True


count = 0
for i in g:
    if number(i):
        count += 1
print(count)
