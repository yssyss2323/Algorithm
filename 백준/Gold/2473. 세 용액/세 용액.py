n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()
arr2 = [-arr1[i] for i in range(n - 1, -1, -1)]

def bisect(arr, x):
    r, l = 0, len(arr) - 1
    while r <= l:
        m = (r + l) // 2
        if arr[m] < x:
            r = m + 1
        elif arr[m] > x:
            l = m - 1
        else:
            return m
    return m


val = float('inf')
ans = []

for i in range(n - 1):
    for j in range(i):
        x = arr1[i] + arr1[j]
        idx = bisect(arr2, x)
        check = [-arr2[max(0, idx - 1)], -arr2[idx], -arr2[min(n - 1, idx + 1)]]
        for c in check:
            if c == arr1[i] or c == arr1[j]:
                continue
            tmp = abs(x + c)
            if val > tmp:
                val = tmp
                ans = [arr1[i], arr1[j], c]
ans.sort()
print(*ans)