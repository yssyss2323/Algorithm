n = int(input()) // 2

ans = (n * 2 - 1) * 4
last = int(n / 2 ** 0.5)
for i in range(1, last + 1):
    check_num = (n - i) * (n + i)
    tmp = check_num ** 0.5
    if int(tmp) ** 2 == check_num:
        ans -= 8
print(ans)