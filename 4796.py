i = 0

while 1:
    count = 0
    L, P, V = map(int, input().split())

    if L == 0 and P == 0 and V == 0:
        break

    count += V // P * L
    V %= P

    if V / L >= 1:
        count += L
    else:
        count += V

    print('Case '+str(i+1)+': '+str(count), sep='')

    i += 1
