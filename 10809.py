g = list(input())
ans = []

for i in range(26):
    if chr(97+i) in g:
        ans.append(g.index(chr(97+i)))
    else:
        ans.append(-1)
print(*ans)
