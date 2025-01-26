import sys
input = sys.stdin.readline

n, m = map(int, input().split())

size = 0
while 2 ** size < n:
    size += 1

seg = [0 for _ in range(2 ** (size + 1))]

for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 0:
        start = 2 ** size + min(b, c) - 1
        end = 2 ** size + max(b, c) - 1
        ans = 0
        while start <= end:
            if start % 2 == 1:
                ans += seg[start]
            if end % 2 == 0:
                ans += seg[end]
            start = (start + 1) // 2
            end = (end - 1) // 2
        print(ans)
    else:
        idx = 2 ** size + b - 1
        gap = c - seg[idx]
        seg[idx] = c
        while idx > 1:
            idx //= 2
            seg[idx] += gap
