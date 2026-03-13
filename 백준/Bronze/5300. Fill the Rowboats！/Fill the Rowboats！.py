n = int(input())

ans = []
for i in range(n // 6):
    ans += [i * 6 + j for j in range(1, 7)]
    ans += ["Go!"]
if n % 6:
    ans += [(n // 6) * 6 + j for j in range(1, n % 6 + 1)]
    ans += ["Go!"]
print(*ans)