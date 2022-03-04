from sys import stdin, stdout
input = stdin.readline

T = int(input())

for i in range(T):
    n = int(input())
    s = sorted([list(map(int, stdin.readline().split())) for j in range(n)])

    tmp = s[0][1]
    count = 1

    for i in range(1, n):
        if tmp > s[i][1]:
            count += 1
            tmp = s[i][1]

    print(count)
