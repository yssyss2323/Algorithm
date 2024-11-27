t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    standard = arr[n - 1]
    ans = 0
    for i in range(n - 2, -1, -1):
        curr = arr[i]
        if curr <= standard:
            ans += standard - curr
        else:
            standard = curr
    print(ans)