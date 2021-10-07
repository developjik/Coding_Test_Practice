arr = list(input().upper())
arr_search = list(set(arr))

ans = [arr.count(i) for i in arr_search]

print('?') if ans.count(max(ans)) > 1 else print(
    arr_search[ans.index(max(ans))])
