def f(a,b,x):
    ha = (a ** 2 - x ** 2) ** 0.5
    hb = (b ** 2 - x ** 2) ** 0.5
    return 1 / (1 / ha + 1 / hb)

a,b,c = map(float, input().split())
start, end = 0, min(a,b)
mid = (start + end) / 2
n = 0
while abs(f(a,b,mid) - c) > 1e-4:
    n += 1
    if f(a,b,mid) < c:
        end = mid
    else:
        start = mid
    mid = (start + end) / 2

print(mid)