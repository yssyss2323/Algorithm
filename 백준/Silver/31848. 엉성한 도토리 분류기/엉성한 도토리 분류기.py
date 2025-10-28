n = int(input())
alist = list(map(int, input().split()))
aalist = [i + alist[i] for i in range(n)]
for i in range(1, n):
    if aalist[i] < aalist[i - 1]:
        aalist[i] = aalist[i - 1]
q = int(input())
slist = list(map(int, input().split()))


ans = []
for s in slist:
    l, r = 0, n
    while l < r:
        m = (l + r) // 2
        if aalist[m] < s:
            l = m + 1
        else:
            r = m
    ans.append(l + 1)
print(*ans)