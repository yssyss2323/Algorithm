n = input()
ans = 1 + (len(n) - 1) * 9
for i in range(1, 10):
    if int(n) >= i * (10 ** len(n) - 1) // 9:
        ans += 1
print(ans)