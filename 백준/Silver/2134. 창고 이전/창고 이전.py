import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
num_object = [int(input()) for _ in range(n)]
num_margin = [int(input()) for _ in range(m)]

x, y = sum(num_object), sum(num_margin)
ans1, ans2 = 0, 0
for i in range(n):
    tmp = num_object[i]
    if ans1 + tmp > y:
        tmp = y - ans1
        ans1 += tmp
        ans2 += (i + 1) * tmp
        break
    else:
        ans1 += tmp
        ans2 += (i + 1) * tmp

tot = 0
for i in range(m):
    tmp = num_margin[i]
    if tot + tmp > ans1:
        tmp = ans1 - tot
        ans2 += (i + 1) * tmp
        break
    else:
        tot += tmp
        ans2 += (i + 1) * tmp
print(ans1, ans2)