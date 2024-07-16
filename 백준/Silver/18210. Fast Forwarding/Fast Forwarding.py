n = int(input())

x = 0
cnt = 0
ans = 0
while 3 * x + 4 <= n:
    x = 3 * x + 4
    cnt += 1
    ans += 2
n -= x
for i in range(cnt, -1, -1):
    tmp, n = divmod(n, 3 ** i)
    ans += tmp

print(ans)