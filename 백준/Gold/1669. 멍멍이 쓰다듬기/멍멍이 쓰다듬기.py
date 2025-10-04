x, y = map(int, input().split())

gap = y - x
if gap <= 3:
    print(gap)
else:
    n = int(gap ** 0.5)
    if n == gap ** 0.5:
        print(2 * n - 1)
    elif gap <= n * (n + 1):
        print(2 * n)
    else:
        print(2 * n + 1)