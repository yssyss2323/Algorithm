import sys
input = sys.stdin.readline

def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

for _ in range(int(input())):
    a, b, c = map(int, input().split())

    if c % gcd(a, b) == 0 and c <= max(a, b):
        print("YES")
    else:
        print("NO")