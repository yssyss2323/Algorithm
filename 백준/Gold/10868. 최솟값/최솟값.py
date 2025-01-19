import sys
input = sys.stdin.readline

n, m = map(int, input().split())
size = 0
while 2 ** size < n:
    size += 1
seg = [float('inf') for _ in range(2 ** (size + 1))]
for i in range(n):
    seg[2 ** size + i] = int(input())

for i in range(size):
    for j in range(2 ** (size - i), 2 ** (size - i + 1), 2):
        seg[j // 2] = min(seg[j], seg[j + 1])

for _ in range(m):
    a, b = map(int, input().split())
    start, end = a + 2 ** size - 1, b + 2 ** size - 1
    ans = float('inf')
    while start <= end:

        if start % 2 == 1:
            ans = min(ans, seg[start])
        if end % 2 == 0:
            ans = min(ans, seg[end])
        start = (start + 1) // 2
        end = (end - 1) // 2
    print(ans)
