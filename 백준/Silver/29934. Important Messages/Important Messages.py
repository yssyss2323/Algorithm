import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
contact_list = []
for _ in range(N):
    contact_list.append(input())
M = int(input())
ans = 0
for _ in range(M):
    if input() in contact_list:
        ans += 1
print(ans)