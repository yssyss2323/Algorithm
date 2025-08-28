n, k = map(int, input().split())

if k * (k + 1) // 2 > n:
    print(-1)
else:
    print(k if (n * 2) % k else k - 1)