from collections import deque
q = list(input())
q = []
ans = 0

for i in g:

    if i == ')':
        t = 0

        while q:
            p = q.pop()

            if p == '(':
                if t == 0:
                    q.append(2)
                else:
                    q.append(2 * t)
                break
            elif p == '[':
                print(0)
                exit(0)
            else:
                t += p

    elif i == ']':
        t = 0

        while q:
            p = q.pop()

            if p == '[':
                if t == 0:
                    q.append(3)
                else:
                    q.append(3 * t)
                break
            elif p == '(':
                print(0)
                exit(0)
            else:
                t += p

    else:
        q.append(i)


for i in q:
    if i == '(' or i == '[':
        print(0)
        exit(0)
    else:
        ans += i

print(ans)
