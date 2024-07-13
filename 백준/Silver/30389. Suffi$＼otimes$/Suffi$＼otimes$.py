import sys
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
sdic = dict()
for _ in range(n):
    s = input()
    for i in range(len(s)):
        tmp = s[i:]
        sdic[tmp] = sdic.get(tmp, 0) + 1
ans = 0
for key, val in sdic.items():
    if val % 2:
        ans += 1
print(ans)