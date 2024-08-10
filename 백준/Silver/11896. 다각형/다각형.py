def f(x):
    if x <= 1:
        return 0
    return x * (x + 1) - 2

n, m = map(int, input().split())
n = (n - 1) // 2
m //= 2
print(f(m) - f(n))