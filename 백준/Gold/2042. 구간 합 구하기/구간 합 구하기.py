import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
size = 0
while 2 ** size < n:
    size += 1
seg = [0 for _ in range(2 ** (size + 1))]
for i in range(n):
    seg[2 ** size + i] = int(input())
for i in range(size):
    for j in range(2 ** (size - i), 2 ** (size - i + 1), 2):
        seg[j // 2] = seg[j] + seg[j + 1]

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        tmp = b + 2 ** size - 1
        diff = c - seg[tmp]
        while tmp > 0:
            seg[tmp] += diff
            tmp //= 2
    else:
        start, end = b + 2 ** size - 1, c + 2 ** size - 1
        ans = 0
        while start <= end:
            if start % 2 == 1:
                ans += seg[start]
            if end % 2 == 0:
                ans += seg[end]
            start = (start + 1) // 2
            end = (end - 1) // 2
        print(ans)
