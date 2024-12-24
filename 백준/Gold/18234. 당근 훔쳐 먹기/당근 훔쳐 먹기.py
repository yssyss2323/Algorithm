import sys
input = sys.stdin.readline

n, t = map(int, input().split())
wlist, plist = [], []
for _ in range(n):
    w, p = map(int, input().split())
    wlist.append(w)
    plist.append(p)
plist.sort()
ans = sum(wlist) + sum([(i + t - n)* plist[i] for i in range(n)])
print(ans)