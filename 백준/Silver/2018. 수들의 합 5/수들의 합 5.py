def calc(n):
    return n * (n + 1) // 2

n = int(input())
s, e = 0, 1
ans = 0
while s < e:
    if calc(e) - calc(s) < n:
        e += 1
    elif calc(e) - calc(s) > n:
        s += 1
    else:
        ans += 1
        s += 1
        e += 1
print(ans)