n = int(input())
ans = 0
for _ in range(n):
    a, b, c = map(int, input().split())
    if a == b == c:
        tmp = 10000 + a * 1000
    elif a == b or a == c:
        tmp = 1000 + a * 100
    elif b == c:
        tmp = 1000 + b * 100
    else:
        tmp = max(a, b, c) * 100
    if tmp > ans:
        ans = tmp
print(ans)