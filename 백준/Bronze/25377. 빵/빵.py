n = int(input())
ans = -1
for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        continue
    else:
        if ans == -1:
            ans = b
        else:
            ans = min(ans, b)
print(ans)