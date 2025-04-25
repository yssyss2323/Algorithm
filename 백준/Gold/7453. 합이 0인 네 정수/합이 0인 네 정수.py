from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
alist, blist, clist, dlist = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    alist.append(a)
    blist.append(b)
    clist.append(c)
    dlist.append(d)

ab_count = defaultdict(int)
for a in alist:
    for b in blist:
        ab_count[a + b] += 1

ans = 0
for c in clist:
    for d in dlist:
        target = -(c + d)
        if target in ab_count:
            ans += ab_count[target]

print(ans)