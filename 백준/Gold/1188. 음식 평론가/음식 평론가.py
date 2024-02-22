def gcd(x,y):
    z = x % y
    if z == 0:
        return y
    else:
        return gcd(y,z)

n, m = map(int,input().split())
t = gcd(n,m)
m //= t
print((m-1)*t)