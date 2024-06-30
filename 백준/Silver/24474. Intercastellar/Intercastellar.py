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
    idx = 0
    now_q = int(input())
    for i in range(idx, n):
        if now_q <= alist[i][1]:
            print(alist[i][0])
            idx = i
            break