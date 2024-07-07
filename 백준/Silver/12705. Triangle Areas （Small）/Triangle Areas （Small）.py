c = int(input())
for i in range(c):
    n, m, a = map(int, input().split())
    if a > n * m:
        ans = 'IMPOSSIBLE'
    else:
        p, q = divmod(a, m)
        if q:
            x2, y2 = p + 1, m - q
            x3, y3 = 1, m
        else:
            x2, y2 = p, 0
            x3, y3 = 0, m
        ans = ' '.join(map(str, [0, 0, x2, y2, x3, y3]))
    print(f"Case #{i + 1}: {ans}")
