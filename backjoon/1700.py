N, K = map(int, input().split())

arr = list(map(int, input().split()))

plugs = []
count = 0

for i in range(len(arr)):
    if arr[i] in plugs:
        continue
    if len(plugs) < N:
        plugs.append(arr[i])
        continue

    swap = 0
    for j in plugs:
        if j not in arr[i:]:
            swap = j
            break


print(count)
