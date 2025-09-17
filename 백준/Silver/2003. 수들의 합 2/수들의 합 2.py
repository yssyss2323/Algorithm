n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0]
tmp = 0
for i in range(n):
    tmp += arr[i]
    prefix_sum.append(tmp)

s, e = 0, 1
ans = 0
while e <= n:
    if e == n and prefix_sum[e] - prefix_sum[s] < m:
        break
    if prefix_sum[e] - prefix_sum[s] == m:
        ans += 1
        s += 1
        e += 1
    elif prefix_sum[e] - prefix_sum[s] > m:
        s += 1
    else:
        e += 1
print(ans)
