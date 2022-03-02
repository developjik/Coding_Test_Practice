def number(x):
    if x == 1:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False

    return True

n = int(input())
g = [ i for i in map(int, input().split()) if number(i) ]

print(len(g))
