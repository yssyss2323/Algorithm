import sys
input = sys.stdin.readline

n = int(input())
ans = 0
price = float('inf')
for i in range(n):
    p,d = input().split()
    if '0' in d and '1' in d and d.count('2') > 1:
        if int(p) < price:
            price = int(p)
            ans = i + 1
print(ans)