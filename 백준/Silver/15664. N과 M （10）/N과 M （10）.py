n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
check = {i:0 for i in num}
ans = set()
def bt(arr, dic, length):
    if len(arr) == length:
        arr = tuple(arr)
        if arr not in ans:
            ans.add(arr)
            print(*arr)
        return

    for i in range(n):
        curr = num[i]
        if dic[curr] >= num.count(curr):
            continue
        if arr and curr < arr[-1]:
            continue
        arr.append(curr)
        dic[curr] += 1
        bt(arr, dic, length)
        dic[curr] -= 1
        arr.pop()

bt([], check, m)