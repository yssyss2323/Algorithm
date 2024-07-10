primelist = [False, False] + [True] * 999999
for i in range(2, 1001):
    if primelist[i]:
        for j in range(2 * i, 1000001, i):
            primelist[j] = False

t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(2, n // 2 + 1):
        if primelist[i] and primelist[n - i]:
            cnt += 1
    print(cnt)
