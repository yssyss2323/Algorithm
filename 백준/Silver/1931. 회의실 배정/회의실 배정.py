import sys
input = lambda:sys.stdin.readline().rstrip()

N = int(input())
time_table = []
for _ in range(N):
    start, end = map(int,input().split())
    time_table.append([end, start])
time_table.sort()

now = 0
ans = 0
for i in range(N):
    if now <= time_table[i][1]:
        now = time_table[i][0]
        ans += 1
print(ans)