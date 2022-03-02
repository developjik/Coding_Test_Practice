from sys import stdin

_ = stdin.readline()
N = sorted((map(int, stdin.readline().split())))

_ = stdin.readline()
M = list(map(int, stdin.readline().split()))


def binarySearch(target, N, start, end):

    if start > end:
        return 0

    mid = (start + end) // 2

    if target == N[mid]:
        return N[start:end+1].count(target)
    elif target <= N[mid]:
        return binarySearch(target, N, start, mid-1)
    else:
        return binarySearch(target, N, mid+1, end)


ans = {}

for i in range(len(M)):
    start = 0
    end = len(N) - 1

    if M[i] not in ans:
        ans[M[i]] = (binarySearch(M[i], N, start, end))

print(*[ans[i] for i in M])