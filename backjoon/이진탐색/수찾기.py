N = int(input())
N_L = list(map(int, input().split()))
N_L.sort()

M = int(input())
M_L = list(map(int, input().split()))

def binarySearch(target, N_L):
    start = 0
    end = len(N_L)-1

    while start <= end:
        mid = (start + end) // 2

        if target == N_L[mid]:
            print(1)
            return
        elif target >= N_L[mid]:
            start = mid+1
        else:
            end = mid-1

    print(0)
    
    return

for i in range(M):
    binarySearch(M_L[i], N_L)
