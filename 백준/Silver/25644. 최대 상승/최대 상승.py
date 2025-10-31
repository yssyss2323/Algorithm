n = int(input())
alist = list(map(int, input().split()))

s, e = alist[0], alist[0]
ans = 0
for i in range(1, n):
    if alist[i] < s:
        s = alist[i]
        e = alist[i]
    if alist[i] > e:
        e = alist[i]
        if ans < e - s:
            ans = e - s
print(ans)