import sys
input = sys.stdin.readline

n = int(input())
xlist, ylist = [], []
for _ in range(n):
    x, y = map(int, input().split())
    xlist.append(x)
    ylist.append(y)
xlist.sort()
ylist.sort()

x, y = xlist[n // 2], ylist[n // 2]
ans = 0
for i in range(n):
    ans += abs(xlist[i] - x)
    ans += abs(ylist[i] - y)
print(ans)