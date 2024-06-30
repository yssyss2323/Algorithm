import sys
input = sys.stdin.readline

n = int(input())
alist = []
tmp_sum = 0
for _ in range(n):
    a = int(input())
    cnt = 0
    while a % 2 == 0:
        a //= 2
        cnt += 1
    tmp_sum += 2 ** cnt
    alist.append([a, tmp_sum])
q = int(input())
qlist = []
for _ in range(q):
    now_q = int(input())
    l, r = 0, n - 1
    while l <= r:
        m = (l + r) // 2
        if now_q > alist[m][1]:
            l = m + 1
        elif now_q < alist[m][1]:
            r = m - 1
        else:
            break
    if alist[m][1] < now_q:
        ans = alist[m+1][0]
    else:
        ans = alist[m][0]
    print(ans)
