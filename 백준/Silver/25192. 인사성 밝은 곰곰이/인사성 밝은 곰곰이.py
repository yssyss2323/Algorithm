import sys

input = lambda:sys.stdin.readline().rstrip()

n = int(input())
check = []
idx = []
for i in range(n):
    tmp = input()
    check.append(tmp)
    if tmp == 'ENTER':
        idx.append(i)
idx.append(n)
ans = 0
for i in range(len(idx)-1):
    ans += len(set(check[idx[i]+1:idx[i+1]]))
print(ans)