a = [list(input().split()) for _ in range(int(input()))]
a = [[i[0], int(i[1]), int(i[2]), int(i[3])] for i in a]
a.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in a:
    print(i[0])
