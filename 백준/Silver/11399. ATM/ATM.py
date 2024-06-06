import sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
P = list(map(int,input().split()))
P.sort()
ans, tmp = 0, 0
for p in P:
    tmp += p
    ans += tmp
print(ans)