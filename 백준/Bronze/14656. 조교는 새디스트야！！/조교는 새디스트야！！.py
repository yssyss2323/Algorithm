n = int(input())
arr = list(map(int, input().split()))

ans = 0
for i in range(1, n + 1):
    if arr[i - 1] != i:
        ans += 1
print(ans)