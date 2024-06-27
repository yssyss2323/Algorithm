n = int(input())
m = int(((n - 1) / 3) ** 0.5)
if 1 + 3 * m * (m + 1) < n:
    print(m + 2)
else:
    print(m + 1)