n, k = map(int, input().split())
arr = list(map(int, input().split()))

tmp = sum(arr[:k])
ans = tmp
for i in range(n - k):
    tmp += arr[i + k] - arr[i]
    if tmp > ans:
        ans = tmp

print(ans)