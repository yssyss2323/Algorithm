def check(n):
    tmp, i = 0, 0
    while tmp < n:
        i += 1
        tmp += i
    value = 0
    for j in range(i + 1):
        value += j ** 2
    value -= (tmp - n) * i
    return value

a, b = map(int, input().split())
print(check(b) - check(a - 1))