n = int(input())
m = int(input())
arr = set(map(int, input().split()))

ans = 0
for i in arr:
    if m - i in arr:
        ans += 1
print(ans // 2)