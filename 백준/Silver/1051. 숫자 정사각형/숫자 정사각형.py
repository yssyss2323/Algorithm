n, m = map(int, input().split())
rect = [input() for _ in range(n)]
limit = min(n, m)
ans = 1
for i in range(2, limit + 1):
    for a in range(n - i + 1):
        found = False
        for b in range(m - i + 1):
            if rect[a][b] == rect[a + i - 1][b] == rect[a][b + i - 1] == rect[a + i - 1][b + i - 1]:
                ans = i ** 2
                found = True
                break
        if found:
            break
print(ans)