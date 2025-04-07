n, m = map(int, input().split())
alist = list(map(int, input().split()))
mod_sum = [1] + [0] * (m - 1)

tmp = 0
for i in range(n):
    tmp += alist[i]
    tmp %= m
    mod_sum[tmp] += 1

ans = 0
for ms in mod_sum:
    if ms >= 2:
        ans += ms * (ms - 1) // 2
print(ans)