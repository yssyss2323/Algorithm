def lcm(x, y):
    def gcd(x, y):
        if y == 0:
            return x
        return gcd(y, x % y)
    return x * y // gcd(x, y)


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(lcm(a, b))
