n = int(input())
alist = list(map(int, input().split()))

def bisect_left(arr, x):
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l

dp = []
dp_idx = []

for i in range(n):
    a = alist[i]
    idx = bisect_left(dp, a)
    if idx == len(dp):
        dp.append(a)
    else:
        dp[idx] = a
    dp_idx.append(idx)


length = len(dp)
print(length)
res = []
for i in range(n - 1, -1, -1):
    if dp_idx[i] == length - 1:
        res.append(alist[i])
        length -= 1
print(*res[::-1])
