import sys
input = lambda:sys.stdin.readline().rstrip()

m,n = map(int,input().split())
book = [input() for _ in range(m)]
ans = 0
for _ in range(n):
    tmp = input()
    for i in range(m):
        if tmp in book[i]:
            ans += 1
            break
print(ans)