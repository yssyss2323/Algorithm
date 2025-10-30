n, m = map(int, input().split())
sx, sy = map(int, input().split())
ex, ey = map(int, input().split())

if n == 1:
    if (sx, sy) == (ex, ey):
        print("YES")
    else:
        print("NO")
elif m == 1:
    if (sx, sy) == (ex, ey):
        print("YES")
    else:
        print("NO")
else:
    if (sx + sy) % 2 == (ex + ey) % 2:
        print("YES")
    else:
        print("NO")