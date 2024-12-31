s = input()
t = input()

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

length = len(s) * len(t) // gcd(len(s), len(t))
ss = s * (length // len(s))
tt = t * (length // len(t))
print(1 if ss == tt else 0)