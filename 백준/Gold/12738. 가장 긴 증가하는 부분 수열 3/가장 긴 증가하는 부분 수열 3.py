n = int(input())
nums = list(map(int, input().split()))

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
for i in range(n):
    curr = nums[i]
    idx = bisect_left(dp, curr)
    if idx == len(dp):
        dp.append(curr)
    else:
        dp[idx] = curr
print(len(dp))