g = list(input())

for i in g:

    if 68 <= ord(i) <= 90:
        print(chr(ord(i)-3), end='')
    else:
        print(chr(ord(i)+26-3), end='')
