tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

a, b = map(int, input().split())
answer = ''

while a != 0:

    answer += str(tmp[a % b])
    a = a // b

print(answer[::-1])
