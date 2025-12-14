n, l = map(int, input().split())

for i in range(l, 101):
    tmp = n - i * (i - 1) // 2
    if tmp < 0:
        continue
    if tmp % i == 0:
        start = tmp // i
        ans = [x for x in range(start, start + i)]
        print(*ans)
        break
else:
    print(-1)