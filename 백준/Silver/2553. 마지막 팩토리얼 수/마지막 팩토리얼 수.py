n = int(input())
if n == 1:
    print(1)
else:
    cnt_2, cnt_5 = 0, 0
    n1, n2 = n, n
    while n1 > 0:
        n1 //= 2
        cnt_2 += n1
    while n2 > 0:
        n2 //= 5
        cnt_5 += n2
    arr = [6, 2, 4, 8]
    cnt = arr[(cnt_2 - cnt_5) % 4]

    ans = 1
    for i in range(1, n + 1):
        while i % 2 == 0:
            i //= 2
        while i % 5 == 0:
            i //= 5
        ans *= i
        ans %= 10
    ans *= cnt
    ans %= 10
    print(ans)