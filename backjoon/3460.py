for _ in range(int(input())):
    b = bin(int(input()))[2:]
    b = b[::-1]

    for i in range(len(b)):
        if b[i] == '1':
            print(i, end=' ')
