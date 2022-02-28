N = int(input())
arr = sorted([int(input())for _ in range(N)], reverse=True)
w = []

for i in range(N):
    w.append(arr[i]*(i+1))

print(max(w))
