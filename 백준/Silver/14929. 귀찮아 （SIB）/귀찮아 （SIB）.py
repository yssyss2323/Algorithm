n = int(input())
arr = list(map(int, input().split()))

tot = sum(arr)
ans = 0
for i in range(n - 1):
    tot -= arr[i]
    ans += arr[i] * tot
print(ans)