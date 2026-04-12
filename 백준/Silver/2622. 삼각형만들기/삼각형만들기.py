n = int(input())
ans = 0
for i in range((n - 3) // 3 + 1, (n - 1) // 2 + 1):
    ans += i - (n - i + 1) // 2 + 1
print(ans)