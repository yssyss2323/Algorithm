import sys


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


n = int(sys.stdin.readline())
coords = dict()
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    tmp = abs(gcd(x, y))
    x //= tmp
    y //= tmp
    coords[(x, y)] = coords.get((x, y), 0) + 1
print(max(coords.values()))
