def lcm(a, b, c):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)

    def lcm(a, b):
        return a * b // gcd(a, b)

    return lcm(lcm(a, b), c)


p1, p2, p3, x1, x2, x3 = map(int, input().split())
ps = [p1, p2, p3]
xs = [x1, x2, x3]
p = lcm(p1, p2, p3)
s = [set(), set(), set()]
for i in range(3):
    for j in range(p // ps[i]):
        s[i].add(j * ps[i] + xs[i])

final = s[0].intersection(s[1].intersection(s[2]))
print(min(final) if final else -1)