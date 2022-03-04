# from sys import stdin
# from itertools import combinations

# input = stdin.readline
# n = int(input())

# nums = []
# for i in range(1, 11):
#     for comb in combinations(range(0, 10), i):
#         comb = list(comb)
#         comb.sort(reverse=True)
#         nums.append(int("".join(map(str, comb))))

# nums.sort()

# try:
#     print(nums[n])
# except:
#     print(-1)


from sys import setrecursionlimit, stdin

input = stdin.readline
setrecursionlimit(10 ** 9)

def solve(n):
    cnt = 0
    num = 1

    while True:
        str_num = str(num)
        flag = True
        if len(str_num) == 1:  # 길이가 1이면 무조건 감소하는 수
            pass
        else:
            for i in range(1, len(str_num)):
                if int(str_num[i]) < int(str_num[i - 1]):
                    continue    
                else:
                    print(num)
                    start = str_num[:i - 1]
                    mid = str(int(str_num[i - 1]) + 1)
                    end = '0' + str_num[i + 1:]
                    num = int(start + mid + end)
                    print(num)
                    print(start, mid, end)
                    print()
                    flag = False
                    break
        if flag:
            cnt += 1
            if cnt == n:  # n번째 감소하는 수
                return num
            num += 1


if __name__ == "__main__":
    n = int(input())
    if n >= 1023:  # 1022: 9876543210
        print(-1)  # N번째 감소하는 수 x
    elif n == 0:
        print(0)
    else:
        print(solve(n))