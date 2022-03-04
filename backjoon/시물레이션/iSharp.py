from sys import stdin, stdout

input = stdin.readline
print = stdout.write

arr = input()[:-1].replace(",", "").split()

for i in range(1, len(arr)):

    print(arr[0], end='')

    for j in range(len(arr[i])-1, -1, -1):

        if not arr[i][j].isalpha():
            if arr[i][j] == "[":
                print("]", end='')
            elif arr[i][j] == "]":
                print("[", end='')
            else:
                print(arr[i][j], end='')

    print(" ", end='')

    for j in range(0, len(arr[i])):

        if arr[i][j].isalpha():
            print(arr[i][j], end='')

    print(";")
