n, m = map(int, input().split())
ans = n // m
if n % m:
    ans += 1
print(ans)