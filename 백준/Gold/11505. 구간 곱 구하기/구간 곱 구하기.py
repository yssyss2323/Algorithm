import sys
input = sys.stdin.readline
MOD = 1000000007

n, m, k = map(int, input().split())
height = 0
while 2 ** height < n:
    height += 1
seg = [1 for _ in range(2 ** (height + 1))]
for i in range(n):
    seg[2 ** height + i] = int(input())
for i in range(1, height + 1):
    for j in range(2 ** (height - i), 2 ** (height - i + 1)):
        seg[j] = (seg[j * 2] * seg[j * 2 + 1]) % MOD

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        idx = 2 ** height + b - 1
        seg[idx] = c
        while idx > 1:
            idx //= 2
            seg[idx] = (seg[idx * 2] * seg[idx * 2 + 1]) % MOD
    else:
        ans = 1
        start = 2 ** height + b - 1
        end = 2 ** height + c - 1
        while start <= end:
            if start % 2 == 1:
                ans = (ans * seg[start]) % MOD
            if end % 2 == 0:
                ans = (ans * seg[end]) % MOD
            start = (start + 1) // 2
            end = (end - 1) // 2
        print(ans)