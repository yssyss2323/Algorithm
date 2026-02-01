n = int(input())
x = n // 100
if n >= 1000000:
    x *= 20
elif n >= 500000:
    x *= 15
elif n >= 100000:
    x *= 10
else:
    x *= 5
print(x, n - x)
