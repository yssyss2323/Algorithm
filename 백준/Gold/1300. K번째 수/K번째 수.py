n = int(input())
k = int(input())

r = 1
l = n ** 2

while r <= l:
    m = (r + l) // 2
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(m // i, n)
    if cnt > k - 1:
        ans = m
        l = m - 1
    else:
        r = m + 1
print(ans)