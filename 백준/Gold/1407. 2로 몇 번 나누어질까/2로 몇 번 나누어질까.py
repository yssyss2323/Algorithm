def func(x):
    cnt = x
    lev = 0
    while x // 2 > 0:
        cnt += (x // 2) * (2 ** lev)
        x //= 2
        lev += 1
    return cnt

a, b = map(int, input().split())
print(func(b) - func(a - 1))