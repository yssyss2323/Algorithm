n = int(input())
a, b, c = map(int, input().split())

ans = min(a, n) + min(b, n) + min(c, n)
print(ans)